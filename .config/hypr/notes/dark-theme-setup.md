# Dark Theme Setup

## Packages Installed
```bash
sudo pacman -S adwaita-qt5 adwaita-qt6 qt5ct qt6ct
```

## Changes Made

### 1. GTK3 — `~/.config/gtk-3.0/settings.ini`
```ini
[Settings]
gtk-theme-name = Adwaita-dark
gtk-application-prefer-dark-theme = 1
gtk-cursor-theme-name = Adwaita
gtk-cursor-theme-size = 24
gtk-font-name = Sans 11
gtk-icon-theme-name = Adwaita
```

### 2. GTK4 — `~/.config/gtk-4.0/settings.ini`
```ini
[Settings]
gtk-application-prefer-dark-theme = 1
gtk-cursor-theme-name = Adwaita
gtk-cursor-theme-size = 24
gtk-font-name = Sans 11
gtk-icon-theme-name = Adwaita
```

### 3. gsettings (GTK4 / Electron apps)
```bash
gsettings set org.gnome.desktop.interface color-scheme prefer-dark
gsettings set org.gnome.desktop.interface gtk-theme Adwaita-dark
```

### 4. Environment variables — `~/.config/hypr/hyprland.conf`
```ini
env = GTK_THEME,Adwaita:dark
env = QT_QPA_PLATFORMTHEME,qt5ct
env = QT_STYLE_OVERRIDE,adwaita-dark
```

### 5. Qt5 — `~/.config/qt5ct/qt5ct.conf`
```ini
[Appearance]
style=adwaita-dark
icon_theme=Adwaita
```

### 6. Qt6 — `~/.config/qt6ct/qt6ct.conf`
```ini
[Appearance]
style=adwaita-dark
icon_theme=Adwaita
```

---

## Coverage by App Type

| Toolkit | Apps | Status |
|---|---|---|
| GTK3 | Dolphin, most Linux apps | Adwaita-dark |
| GTK4 | Newer GNOME apps | prefer-dark |
| Qt5 | Some KDE/Qt apps | adwaita-dark via qt5ct |
| Qt6 | Newer Qt apps | adwaita-dark via qt6ct |
| Electron | VS Code, Discord, etc. | Follows color-scheme (prefer-dark) |

## Notes
- Already open apps need to be reopened to pick up the theme
- A full logout/login ensures all env vars are applied correctly
- Qt apps may need `qt5ct` or `qt6ct` run once manually to verify settings
