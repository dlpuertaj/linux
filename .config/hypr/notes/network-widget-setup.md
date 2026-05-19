# Network Widget Setup

## Package Installed
```bash
sudo pacman -S networkmanager-dmenu
```

## How It Works
Clicking the network icon in waybar opens a wofi popup listing available Wi-Fi networks. Selecting one connects to it and prompts for a password if needed.

## Files

### `~/.config/networkmanager-dmenu/config.ini`
Configures networkmanager-dmenu to use wofi with Catppuccin styling, positioned top-right.
```ini
[dmenu]
dmenu_command = wofi --dmenu --prompt "  Network" --width 250 --lines 8 --location top_right --xoffset -10 --yoffset 10

[dmenu_passphrase]
obscure = True
```

### `~/.config/wofi/config`
Global wofi settings.
```ini
width=250
lines=8
prompt=
location=center
allow_markup=true
insensitive=true
no_actions=true
hide_scroll=true
```

### `~/.config/wofi/style.css`
Catppuccin Mocha styling to match the waybar.
- Background: `#1e1e2e`
- Selected item: `#313244` with `#89b4fa` (blue) text
- Font: MesloLGS Nerd Font 13px
- Subtle border and rounded corners

### `~/.config/waybar/config` — network module
```json
"network": {
    "on-click": "networkmanager_dmenu"
}
```
