# Keyboard Layout Persistence Fix

## Problem
Clicking the language icon in waybar switched the layout from US to Latin American Spanish, but it reverted when changing window focus or switching tiles.

## Root Cause
Two issues combined:
1. `hyprctl switchxkblayout` only switches one specific keyboard device temporarily — Hyprland can reset it on window focus change.
2. The system has 8 keyboard devices (video-bus, ite-device, power-button, etc.). Only `at-translated-set-2-keyboard` was being switched, leaving all others on US.

## Fix

### `~/.config/hypr/scripts/kb-layout-toggle.sh`
Replaced `switchxkblayout` with `hyprctl keyword input:kb_layout` which rewrites the running config globally for all devices and persists across window switches.

```bash
#!/bin/bash
CURRENT=$(hyprctl devices -j | python3 -c "
import json, sys
d = json.load(sys.stdin)
for kb in d.get('keyboards', []):
    if kb['name'] == 'at-translated-set-2-keyboard':
        print(kb['active_keymap'].lower())
        break
")

if echo "$CURRENT" | grep -qi "latin\|latam\|spanish"; then
    hyprctl keyword input:kb_layout us
    hyprctl keyword input:kb_variant ""
else
    hyprctl keyword input:kb_layout latam
    hyprctl keyword input:kb_variant ""
fi
```

### `~/.config/waybar/config` — language module
```json
"hyprland/language": {
    "format": "{short}",
    "keyboard-name": "at-translated-set-2-keyboard",
    "on-click": "~/.config/hypr/scripts/kb-layout-toggle.sh",
    "tooltip": false
}
```

## Key Distinction
- `hyprctl switchxkblayout <device> next` — flips layout index on one device, temporary, resets on focus change
- `hyprctl keyword input:kb_layout <layout>` — rewrites running config for ALL devices, persists until next toggle or Hyprland restart
