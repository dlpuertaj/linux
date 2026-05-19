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
