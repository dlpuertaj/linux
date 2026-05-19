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
  *"US"*)   echo "EN" ;;
  *"Spanish"* | *"Latin"*) echo "ES" ;;
  *)        echo "$LAYOUT" ;;
esac
