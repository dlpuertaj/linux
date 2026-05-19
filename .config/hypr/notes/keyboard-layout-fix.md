# Keyboard Layout Switching — Fix Checklist

## Problem
- Clicking the waybar language widget showed "Invalid keyboard layout passed" error
- `hyprctl switchxkblayout` returned "ok" but layout never changed

## Root Cause
`es` with variant `latam` is NOT valid. `latam` is its own standalone xkb layout.

**Wrong:**
```ini
kb_layout = us,es
kb_variant = ,latam
```

**Correct:**
```ini
kb_layout = us,latam
kb_variant = ,
```

Once the layout code was fixed, the built-in `hyprland/language` waybar module worked perfectly.

---

## Solution A — Built-in module (recommended)

### hyprland.conf (`~/.config/hypr/hyprland.conf`)
```ini
input {
    kb_layout = us,latam
    kb_variant = ,
}
```

### Waybar config (`~/.config/waybar/config`)
```json
"hyprland/language": {
    "format": "{short}",
    "keyboard-name": "at-translated-set-2-keyboard",
    "on-click": "hyprctl switchxkblayout at-translated-set-2-keyboard next",
    "tooltip": false
}
```

---

## Solution B — Custom script (fallback)

Use this if the built-in module misbehaves. Shows `EN` / `ES` instead of `us` / `latam`.

### Waybar config (`~/.config/waybar/config`)
```json
"custom/language": {
    "exec": "~/.config/waybar/scripts/keyboard-layout.sh",
    "interval": 2,
    "on-click": "hyprctl switchxkblayout at-translated-set-2-keyboard next",
    "tooltip": false
}
```

### Script (`~/.config/waybar/scripts/keyboard-layout.sh`)
```bash
#!/bin/bash
KEYBOARD="at-translated-set-2-keyboard"
LAYOUT=$(hyprctl devices -j | python3 -c "
import json, sys
d = json.load(sys.stdin)
for k in d['keyboards']:
    if k['name'] == '$KEYBOARD':
        print(k['active_keymap'])
        break
")

case "$LAYOUT" in
  *"US"*)                   echo "EN" ;;
  *"Spanish"* | *"Latin"*)  echo "ES" ;;
  *)                        echo "$LAYOUT" ;;
esac
```

---

## Useful commands

### Find your keyboard device name
```bash
hyprctl devices -j | python3 -c "import json,sys; d=json.load(sys.stdin); [print(k['name']) for k in d['keyboards']]"
```

### Check available xkb layouts
```bash
localectl list-x11-keymap-layouts
```
