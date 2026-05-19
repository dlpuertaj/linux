#!/bin/bash
WALLPAPER_DIR="$HOME/Imágenes/wallpapers"

sleep 1

WALL=$(find "$WALLPAPER_DIR" -type f \( -name "*.jpg" -o -name "*.jpeg" -o -name "*.png" -o -name "*.webp" \) | shuf -n 1)

hyprctl hyprpaper preload "$WALL"

# Apply to all connected monitors dynamically
hyprctl monitors -j | python3 -c "
import json, sys
monitors = json.load(sys.stdin)
for m in monitors:
    print(m['name'])
" | while read -r monitor; do
    hyprctl hyprpaper wallpaper "$monitor,$WALL"
done
