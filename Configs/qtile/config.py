# -*- coding: utf-8 -*-
import os
import re
import socket
import subprocess
from libqtile.config import KeyChord, Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import qtile, layout, bar, widget, hook
from libqtile.lazy import lazy
from typing import List  # noqa: F401

from random import seed
from random import randrange

mod = "mod4"                                     # Sets mod key to SUPER/WINDOWS
myTerm = "alacritty"                             # My terminal of choice
myConfig = "/home/dlpuerta/.config/qtile/config.py"    # The Qtile config file location

keys = [
         ### The essentials
         Key([mod], "Return",
             lazy.spawn(myTerm),
             desc='Launches My Terminal'
             ),
         Key([mod, "shift"], "Return",
             lazy.spawn("dmenu_run -p 'Run: '"),
             #lazy.spawn("rofi -show drun -config ~/.config/rofi/themes/dt-dmenu.rasi -display-drun \"Run: \" -drun-display-format \"{name}\""),
             desc='Run Launcher'
             ),
         Key([mod], "Tab",
             lazy.next_layout(),
             desc='Toggle through layouts'
             ),
         Key([mod, "shift"], "c",
             lazy.window.kill(),
             desc='Kill active window'
             ),
         Key([mod, "shift"], "r",
             lazy.restart(),
             desc='Restart Qtile'
             ),
         Key([mod, "shift"], "q",
             lazy.shutdown(),
             desc='Shutdown Qtile'
             ),
         #Key(["control", "shift"], "e",
         #    lazy.spawn("emacsclient -c -a emacs"),
         #    desc='Doom Emacs'
         #    ),
         ### Switch focus to specific monitor (out of three)
         Key([mod], "w",
             lazy.to_screen(0),
             desc='Keyboard focus to monitor 1'
             ),
         Key([mod], "e",
             lazy.to_screen(1),
             desc='Keyboard focus to monitor 2'
             ),
         #Key([mod], "r",
         #    lazy.to_screen(2),
         #    desc='Keyboard focus to monitor 3'
         #    ),
         ### Switch focus of monitors
         Key([mod], "period",
             lazy.next_screen(),
             desc='Move focus to next monitor'
             ),
         Key([mod], "comma",
             lazy.prev_screen(),
             desc='Move focus to prev monitor'
             ),
         ### Treetab controls
         Key([mod, "control"], "k",
             lazy.layout.section_up(),
             desc='Move up a section in treetab'
             ),
         Key([mod, "control"], "j",
             lazy.layout.section_down(),
             desc='Move down a section in treetab'
             ),
         ### Window controls
         Key([mod], "k",
             lazy.layout.down(),
             desc='Move focus down in current stack pane'
             ),
         Key([mod], "j",
             lazy.layout.up(),
             desc='Move focus up in current stack pane'
             ),
         Key([mod, "shift"], "k",
             lazy.layout.shuffle_down(),
             desc='Move windows down in current stack'
             ),
         Key([mod, "shift"], "j",
             lazy.layout.shuffle_up(),
             desc='Move windows up in current stack'
             ),
         Key([mod], "h",
             lazy.layout.grow(),
             lazy.layout.increase_nmaster(),
             desc='Expand window (MonadTall), increase number in master pane (Tile)'
             ),
         Key([mod], "l",
             lazy.layout.shrink(),
             lazy.layout.decrease_nmaster(),
             desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
             ),
         Key([mod], "n",
             lazy.layout.normalize(),
             desc='normalize window size ratios'
             ),
         Key([mod], "m",
             lazy.layout.maximize(),
             desc='toggle window between minimum and maximum sizes'
             ),
         Key([mod, "shift"], "f",
             lazy.window.toggle_floating(),
             desc='toggle floating'
             ),
         Key([mod, "shift"], "m",
             lazy.window.toggle_fullscreen(),
             desc='toggle fullscreen'
             ),
         ### Stack controls
         Key([mod, "shift"], "space",
             lazy.layout.rotate(),
             lazy.layout.flip(),
             desc='Switch which side main pane occupies (XmonadTall)'
             ),
         Key([mod], "space",
             lazy.layout.next(),
             desc='Switch window focus to other pane(s) of stack'
             ),
         Key([mod, "control"], "Return",
             lazy.layout.toggle_split(),
             desc='Toggle between split and unsplit sides of stack'
             ),
         ### Dmenu scripts launched with ALT + CTRL + KEY
         Key(["mod1", "control"], "e",
             lazy.spawn("./.dmenu/dmenu-edit-configs.sh"),
             desc='Dmenu script for editing config files'
             ),
         Key(["mod1", "control"], "m",
             lazy.spawn("./.dmenu/dmenu-sysmon.sh"),
             desc='Dmenu system monitor script'
             ),
         Key(["mod1", "control"], "p",
             lazy.spawn("passmenu"),
             desc='Passmenu'
             ),
         Key(["mod1", "control"], "r",
             desc='Dmenu reddio script'
             ),
         Key(["mod1", "control"], "s",
             lazy.spawn("./.dmenu/dmenu-surfraw.sh"),
             desc='Dmenu surfraw script'
             ),
         Key(["mod1", "control"], "t",
             lazy.spawn("./.dmenu/dmenu-trading.sh"),
             desc='Dmenu trading programs script'
             ),
         Key(["mod1", "control"], "i",
             lazy.spawn("./.dmenu/dmenu-scrot.sh"),
             desc='Dmenu scrot script'
             ),
         ### My applications launched with SUPER + ALT + KEY
         Key([mod], "Print",
             lazy.spawn("flameshot gui"),
             desc='Flameshot'
             ),
         #Key([mod, "mod1"], "l",
         #    lazy.spawn(myTerm+" -e lynx gopher://distro.tube"),
         #    desc='lynx browser'
         #    ),
         #Key([mod, "mod1"], "n",
         #    lazy.spawn(myTerm+" -e newsboat"),
         #    desc='newsboat'
         #    ),
         #Key([mod, "mod1"], "r",
         #    lazy.spawn(myTerm+" -e rtv"),
         #    desc='reddit terminal viewer'
         #    ),
         #Key([mod, "mod1"], "e",
         #    lazy.spawn(myTerm+" -e neomutt"),
         #    desc='neomutt'
         #    ),
         #Key([mod, "mod1"], "m",
         #    lazy.spawn(myTerm+" -e sh ./scripts/toot.sh"),
         #    desc='toot mastodon cli'
         #    ),
         #Key([mod, "mod1"], "t",
         #    lazy.spawn(myTerm+" -e sh ./scripts/tig-script.sh"),
         #    desc='tig'
         #    ),
         #Key([mod, "mod1"], "f",
         #    lazy.spawn(myTerm+" -e sh ./.config/vifm/scripts/vifmrun"),
         #    desc='vifm'
         #    ),
         #Key([mod, "mod1"], "j",
         #    lazy.spawn(myTerm+" -e joplin"),
         #    desc='joplin'
         #    ),
         #Key([mod, "mod1"], "c",
         #    lazy.spawn(myTerm+" -e cmus"),
         #    desc='cmus'
         #    ),
         #Key([mod, "mod1"], "i",
         #    lazy.spawn(myTerm+" -e irssi"),
         #    desc='irssi'
         #    ),
         #Key([mod, "mod1"], "y",
         #    lazy.spawn(myTerm+" -e youtube-viewer"),
         #    desc='youtube-viewer'
         #    ),
         #Key([mod, "mod1"], "a",
         #    lazy.spawn(myTerm+" -e ncpamixer"),
         #    desc='ncpamixer'
         #    ),
]

group_names = [("WWW", {'layout': 'monadtall'}),
               ("DEV", {'layout': 'monadtall'}),
               ("SYS", {'layout': 'monadtall'}),
               ("FUN", {'layout': 'max'}),
               ("BVC", {'layout': 'monadtall'})
               ]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group

layout_theme = {"border_width": 2,
                "margin": 2,
                "border_focus": "707070",
                "border_normal": "1D2330"
                }

layouts = [
    #layout.MonadWide(**layout_theme),
    #layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    #layout.Columns(**layout_theme),
    #layout.RatioTile(**layout_theme),
    #layout.VerticalTile(**layout_theme),
    #layout.Matrix(**layout_theme),
    #layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Tile(shift_windows=True, **layout_theme),
    layout.Stack(num_stacks=2),
    layout.TreeTab(
         font = "Ubuntu",
         fontsize = 10,
         sections = ["FIRST", "SECOND"],
         section_fontsize = 11,
         bg_color = "141414",
         active_bg = "90C435",
         active_fg = "000000",
         inactive_bg = "384323",
         inactive_fg = "a0a0a0",
         padding_y = 5,
         section_top = 10,
         panel_width =220
         ),
    layout.Floating(**layout_theme)
]

colors = [["#282c34", "#282c34"], # 0  panel background
          ["#434758", "#434758"], # 1  background for current screen tab
          ["#ffffff", "#ffffff"], # 2  font color for group names
          ["#ff5555", "#ff5555"], # 3  border line color for current tab
          ["#8d62a9", "#8d62a9"], # 4  border line color for other tab and odd widgets
          ["#668bd7", "#668bd7"], # 5  color for the even widgets
          ["#e1acff", "#e1acff"], # 6  window name
          ["#3C403D", "#3C403D"], # 7  Brown Grey
          ["#707070", "#707070"], # 8  Madium Grey
          ["#3F3F3F", "#3F3F3F"], # 9  Dark Grey
          ["#202020", "#202020"], # 10 Blackish
          ["#EEFBFB", "#EEFBFB"], # 11 Shadow of Light Blue
          ["#203647", "#203647"], # 12 Shadow Dark Blue
          ["#4DA8DA", "#4DA8DA"], # 13 Lifghtest Blue
          ["#007CC7", "#007CC7"], # 14 Lighter Blue
          ["#12232E", "#12232E"], # 15 Dark Blue
          ["#DE354C", "#DE354C"], # 16 Bright Red
          ["#3C1874", "#3C1874"], # 17 Pure Purpule
          ["#F3F3F3", "#F3F3F3"], # 18 Cloud
          ["#283747", "#283747"], # 19 Purble Tinted Grey
          ["#932432", "#932432"], # 20 Deep Red
          ["#2C5F2D", "#2C5F2D"], # 21
          ["#db0000", "#db0000"]] # 22 red border color for current tab DLP

color_combos = [(colors[9],colors[20]),(colors[8],colors[9])]

random_combo = randrange(0,2);
print("Random combo = :" + str(random_combo))

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="Ubuntu Mono",
    fontsize = 12,
    padding = 2,
    background=colors[8]
)
extension_defaults = widget_defaults.copy()

#### WIDGETS MOUSE CALLBACKS FUNCTIONS

def init_widgets_list():
    widgets_list = [
              widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.Image(
                       filename = "~/.config/qtile/icons/1650_apex_legends.png",
                       scale = "True",
                       background = colors[0],
                       mouse_callbacks = {'Button1':lambda:qtile.cmd_spawn('dmenu_run')}
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.GroupBox(
                       font = "Ubuntu Bold",
                       fontsize = 9,
                       margin_y = 3,
                       margin_x = 0,
                       padding_y = 5,
                       padding_x = 3,
                       borderwidth = 3,
                       active = colors[2],
                       inactive = colors[2],
                       rounded = False,
                       highlight_color = colors[1],
                       highlight_method = "line",
                       this_current_screen_border = colors[22],
                       this_screen_border = colors [4],
                       other_current_screen_border = colors[0],
                       other_screen_border = colors[0],
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.Prompt(
                       prompt = prompt,
                       font = "Ubuntu Mono",
                       padding = 10,
                       foreground = colors[3],
                       background = colors[1]
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 40,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.WindowName(
                       foreground = colors[2],
                       background = colors[0],
                       padding = 0
                       ),
              #widget.TextBox(
                #       text = '',
                #       background = colors[0],
                #       foreground = colors[8],
                #       padding = 0,
                #       fontsize = 37
                #       ),
             # widget.Net(
              #         interface = "wlp3s0f0",
               #        format = '{down} ↓↑ {up}',
                #       max_chars = 3,
                 #      #foreground = colors[8],
                  #     background = colors[8],
                   #    padding = 5
                    #   ),
              widget.TextBox(
                       text = '',
                       background = colors[0],
                       foreground = color_combos[random_combo][1],#colors[9],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.TextBox(
                       text = " 🌡",
                       padding = 2,
                       foreground = colors[2],
                       background = color_combos[random_combo][1],#colors[9],
                       fontsize = 11
                       ),
              widget.ThermalSensor(
                       foreground = colors[2],
                       background = color_combos[random_combo][1],#colors[9],
                       threshold = 90,
                       padding = 5
                       ),
              widget.TextBox(
                       text='',
                       background = color_combos[random_combo][1],#colors[9],
                       foreground = color_combos[random_combo][0],#colors[8],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.TextBox(
                       text = " ⟳",
                       padding = 2,
                       foreground = colors[2],
                       background = color_combos[random_combo][0],#colors[8],
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e sudo pacman -Syu')},
                       fontsize = 14
                       ),
              widget.CheckUpdates(
                       update_interval = 1800,
                       distro = "Arch_checkupdates",
                       display_format = "{updates} Updates",
                       foreground = colors[2],
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e sudo pacman -Syu')},
                       background = color_combos[random_combo][0],#colors[8]
                       ),
              widget.TextBox(
                       text = '',
                       background = color_combos[random_combo][0],#colors[8],
                       foreground = color_combos[random_combo][1],#colors[9],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.TextBox(
                       text = " 🖬  ",
                       foreground = colors[2],
                       background = color_combos[random_combo][1],#colors[9],
                       mouse_callbacks = {'Button1':lambda:qtile.cmd_spawn(myTerm + ' -e htop')},
                       padding = 0,
                       fontsize = 14
                       ),
              widget.Memory(
                       foreground = colors[2],
                       background = color_combos[random_combo][1],#colors[9],
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
                       padding = 5
                       ),
              widget.TextBox(
                       text = '',
                       background = color_combos[random_combo][1],#colors[9],
                       foreground = color_combos[random_combo][0],#colors[8],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.TextBox(
                       text = " Vol:",
                       foreground = colors[2],
                       background = color_combos[random_combo][0],#colors[8],
                       padding = 0
                       ),
              widget.Volume(
                       foreground = colors[2],
                       background = color_combos[random_combo][0],#colors[8],
                       padding = 5
                       ),
              widget.TextBox(
                       text = '',
                       background = color_combos[random_combo][0],#colors[8],
                       foreground = color_combos[random_combo][1],#colors[9],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.CurrentLayoutIcon(
                       custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                       foreground = colors[0],
                       background = color_combos[random_combo][1],#colors[9],
                       padding = 0,
                       scale = 0.7
                       ),
              widget.CurrentLayout(
                       foreground = colors[2],
                       background = color_combos[random_combo][1],#colors[9],
                       padding = 5
                       ),
              widget.TextBox(
                       text = '',
                       background = color_combos[random_combo][1],#colors[9],
                       foreground = color_combos[random_combo][0],#colors[10],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.Clock(
                       foreground = colors[2],
                       background = color_combos[random_combo][0],#colors[10],
                       padding = 0,
                       format = "%A, %B %d  [ %I:%M%p ]"
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 10,
                       foreground = color_combos[random_combo][1],#colors[0],
                       background = color_combos[random_combo][0],#colors[10]
                       ),
              widget.TextBox(
                       text = '',
                       background = color_combos[random_combo][0],#colors[9],
                       foreground = color_combos[random_combo][1],#colors[10],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.Systray(
                       background = color_combos[random_combo][1],#colors[10],
                       padding = 5
                       ),
              widget.TextBox(
                       text = '',
                       background = color_combos[random_combo][1],#colors[9],
                       foreground = color_combos[random_combo][0],#colors[10],
                       padding = 0,
                       fontsize = 37
                       ),
             # widget.Image(
             #          filename = "~/.config/qtile/icons/xfsm-lock.png",
             #          scale = "False",
             #          background = color_combos[random_combo][0],
             #          mouse_callbacks = {'Button1':lambda:qtile.cmd.spawn('vlock')}
             #          ),
             # widget.Image(
             #          filename = "~/.config/qtile/icons/xfsm-logout.png",
             #          scale = "False",
             #          background = color_combos[random_combo][0],
             #          mouse_callbacks = {'Button1':lazy.shutdown()}
             #          ),
              widget.Image(
                       filename = "~/.config/qtile/icons/xfsm-reboot.png",
                       scale = "False",
                       background = color_combos[random_combo][0],
                       mouse_callbacks = {'Button1':lambda:qtile.cmd_spawn('reboot')}
                       ),
              widget.Image(
                       filename = "~/.config/qtile/icons/system-shutdown-icon.png",
                       scale = "False",
                       background = color_combos[random_combo][0],#colors[10],
                       mouse_callbacks = {'Button1':lambda:qtile.cmd_spawn('shutdown now')}
                       ),
              ]
    return widgets_list

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1                       # Slicing removes unwanted widgets on Monitors 1,3

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2                       # Monitor 2 will display all widgets in widgets_list

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=20,background=color_combos[random_combo][1])),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=1.0, size=20,background=color_combos[random_combo][1]))]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()

def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)

def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)

def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"



@hook.subscribe.startup
def autostart():
    home = os.path.expanduser('~')
    subprocess.call([home + '/Documents/screen_conf.sh'])

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
# -*- coding: utf-8 -*-
import os
import re
