#!/bin/bash

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
