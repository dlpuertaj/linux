# Wallpaper Setup

## How It Works
On every login, hyprpaper starts and a script picks a random wallpaper from `~/Pictures/wallpapers/` and applies it.

## Files

### `~/.config/hypr/hyprpaper.conf`
Base config for hyprpaper (no wallpaper set here — the script handles it).
```ini
splash = false
```

### `~/.config/hypr/scripts/wallpaper-random.sh`
Picks a random wallpaper and applies it via hyprpaper IPC.
```bash
#!/bin/bash
WALLPAPER_DIR="$HOME/Pictures/wallpapers"

sleep 1  # wait for hyprpaper to be ready

WALL=$(find "$WALLPAPER_DIR" -type f \( -name "*.jpg" -o -name "*.jpeg" -o -name "*.png" -o -name "*.webp" \) | shuf -n 1)

hyprctl hyprpaper preload "$WALL"
hyprctl hyprpaper wallpaper "eDP-1,$WALL"
```

### `~/.config/hypr/hyprland.conf`
```ini
exec-once = hyprpaper
exec-once = ~/.config/hypr/scripts/wallpaper-random.sh

# misc section
force_default_wallpaper = 0
disable_hyprland_logo = true
```

## Root Cause of Previous Issue
`force_default_wallpaper = -1` was telling Hyprland to show a random built-in anime mascot wallpaper on every startup, overriding hyprpaper entirely.

## Adding More Wallpapers
Just drop `.jpg`, `.jpeg`, `.png`, or `.webp` files into:
```
~/Pictures/wallpapers/
```
They will be included in the random rotation on next login.
