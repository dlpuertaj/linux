# SDDM Login Screen Setup

## Theme Installed
```bash
paru -S sddm-astronaut-theme
```

## How It Works
SDDM uses the `sddm-astronaut-theme` with a custom Catppuccin Mocha preset.
The login form is centered with a blurred background using your own wallpaper.

## Files

### `/etc/sddm.conf`
```ini
[Autologin]
Session=hyprland

[Theme]
Current=sddm-astronaut-theme
CursorTheme=Adwaita
```

### `/usr/share/sddm/themes/sddm-astronaut-theme/metadata.desktop`
- `ConfigFile` was changed from `Themes/astronaut.conf` to `Themes/catppuccin-mocha.conf`

### `/usr/share/sddm/themes/sddm-astronaut-theme/Themes/catppuccin-mocha.conf`
Custom Catppuccin Mocha preset. Key settings:
- Background: `Backgrounds/custom.jpg` (copied from `~/Pictures/wallpapers/wallpaper.jpg`)
- Colors: `#1e1e2e` bg, `#cdd6f4` text, `#89b4fa` blue accent, `#f38ba8` error red
- Form: centered, partial blur (BlurMax=8, Blur=2.0)
- Virtual keyboard hidden, system buttons visible

### `/usr/share/sddm/themes/sddm-astronaut-theme/Backgrounds/custom.jpg`
Copy of your wallpaper used as the login background. To change it:
```bash
sudo cp ~/Pictures/wallpapers/<new-wallpaper> /usr/share/sddm/themes/sddm-astronaut-theme/Backgrounds/custom.jpg
```

## Preview Without Rebooting
```bash
sddm-greeter-qt6 --test-mode --theme /usr/share/sddm/themes/sddm-astronaut-theme
```

## Notes
- Fish shell does not support `<< EOF` heredocs — use `printf` or write to `/tmp` first then `sudo cp`
- `dwindle:pseudotile` was removed from Hyprland; that line was deleted from `hyprland.conf`
- Available presets in `Themes/`: astronaut, black_hole, cyberpunk, hyprland_kath, japanese_aesthetic, purple_leaves, and more
