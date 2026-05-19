# Power Menu Setup

## How It Works
Clicking the power icon (󰐦) in waybar opens a wofi dmenu with three options: Sleep, Restart, Shutdown.

## Files

### `~/.config/waybar/scripts/power-menu.sh`
Builds the menu and handles the selection:
```bash
SLEEP="󰒲  Sleep"
RESTART="󰜉  Restart"
SHUTDOWN="󰐦  Shutdown"

CHOICE=$(printf "%s\n%s\n%s" "$SLEEP" "$RESTART" "$SHUTDOWN" \
  | wofi --dmenu \
         --prompt "" \
         --lines 3 \
         --width 200 \
         --location top_right \
         --no-actions \
         --hide-scroll \
         --insensitive \
         --style ~/.config/wofi/power-menu.css)

case "$CHOICE" in
  "$SLEEP")    systemctl suspend ;;
  "$RESTART")  systemctl reboot ;;
  "$SHUTDOWN") systemctl poweroff ;;
esac
```

### `~/.config/wofi/power-menu.css`
Standalone stylesheet for the power menu (does not inherit global wofi style).
Key details:
- Search/input field is fully hidden (`display: none` + zeroed padding/margin/opacity)
- Width: 200px, entry padding: 9px 14px for a comfortable size
- Catppuccin Mocha colors matching the rest of the setup
- Selected entry has a left blue (`#89b4fa`) border indicator

## Notes
- The `--style` flag in wofi allows per-invocation stylesheets — used here so the hidden input only affects the power menu, not other wofi instances (network, app launcher)
- `@import` does not work reliably in wofi CSS — the power menu CSS is fully self-contained
- The search field cannot be hidden via a wofi CLI flag, only via CSS
