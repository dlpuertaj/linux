--[[

     Dremora Awesome WM theme 2.0
     github.com/lcpz

--]]

local gears = require("gears")
local lain  = require("lain")
local awful = require("awful")
local wibox = require("wibox")
local dpi   = require("beautiful.xresources").apply_dpi

local os = os
local my_table = awful.util.table or gears.table -- 4.{0,1} compatibility

local theme                                     = {}
theme.dir                                       = os.getenv("HOME") .. "/.config/awesome/themes/dremora"
theme.wallpaper                                 = theme.dir .. "/wall.png"
theme.font                                      = "Terminus 10.5"
theme.taglist_font                              = "Icons 10"
theme.fg_normal                                 = "#747474"
theme.fg_focus                                  = "#DDDCFF"
theme.bg_normal                                 = "#121212"
theme.bg_focus                                  = "#121212"
theme.fg_urgent                                 = "#CC9393"
theme.bg_urgent                                 = "#2A1F1E"
theme.border_width                              = dpi(0)
theme.border_normal                             = "#121212"
theme.border_focus                              = "#292929"
theme.titlebar_bg_focus                         = "#292929"
theme.taglist_fg_focus                          = "#dddcff"
theme.taglist_bg_focus                          = "#121212"
theme.menu_height                               = dpi(16)
theme.menu_width                                = dpi(130)
theme.menu_submenu_icon                         = theme.dir .. "/icons/submenu.png"
theme.awesome_icon                              = theme.dir .."/icons/awesome.png"
theme.taglist_squares_sel                       = theme.dir .. "/icons/square_sel.png"
theme.taglist_squares_unsel                     = theme.dir .. "/icons/square_unsel.png"
theme.layout_tile                               = theme.dir .. "/icons/tile.png"
theme.layout_tileleft                           = theme.dir .. "/icons/tileleft.png"
theme.layout_tilebottom                         = theme.dir .. "/icons/tilebottom.png"
theme.layout_tiletop                            = theme.dir .. "/icons/tiletop.png"
theme.layout_fairv                              = theme.dir .. "/icons/fairv.png"
theme.layout_fairh                              = theme.dir .. "/icons/fairh.png"
theme.layout_spiral                             = theme.dir .. "/icons/spiral.png"
theme.layout_dwindle                            = theme.dir .. "/icons/dwindle.png"
theme.layout_max                                = theme.dir .. "/icons/max.png"
theme.layout_fullscreen                         = theme.dir .. "/icons/fullscreen.png"
theme.layout_magnifier                          = theme.dir .. "/icons/magnifier.png"
theme.layout_floating                           = theme.dir .. "/icons/floating.png"
theme.tasklist_plain_task_name                  = true
theme.tasklist_disable_icon                     = true
theme.useless_gap                               = dpi(2)
theme.titlebar_close_button_focus               = theme.dir .. "/icons/titlebar/close_focus.png"
theme.titlebar_close_button_normal              = theme.dir .. "/icons/titlebar/close_normal.png"
theme.titlebar_ontop_button_focus_active        = theme.dir .. "/icons/titlebar/ontop_focus_active.png"
theme.titlebar_ontop_button_normal_active       = theme.dir .. "/icons/titlebar/ontop_normal_active.png"
theme.titlebar_ontop_button_focus_inactive      = theme.dir .. "/icons/titlebar/ontop_focus_inactive.png"
theme.titlebar_ontop_button_normal_inactive     = theme.dir .. "/icons/titlebar/ontop_normal_inactive.png"
theme.titlebar_sticky_button_focus_active       = theme.dir .. "/icons/titlebar/sticky_focus_active.png"
theme.titlebar_sticky_button_normal_active      = theme.dir .. "/icons/titlebar/sticky_normal_active.png"
theme.titlebar_sticky_button_focus_inactive     = theme.dir .. "/icons/titlebar/sticky_focus_inactive.png"
theme.titlebar_sticky_button_normal_inactive    = theme.dir .. "/icons/titlebar/sticky_normal_inactive.png"
theme.titlebar_floating_button_focus_active     = theme.dir .. "/icons/titlebar/floating_focus_active.png"
theme.titlebar_floating_button_normal_active    = theme.dir .. "/icons/titlebar/floating_normal_active.png"
theme.titlebar_floating_button_focus_inactive   = theme.dir .. "/icons/titlebar/floating_focus_inactive.png"
theme.titlebar_floating_button_normal_inactive  = theme.dir .. "/icons/titlebar/floating_normal_inactive.png"
theme.titlebar_maximized_button_focus_active    = theme.dir .. "/icons/titlebar/maximized_focus_active.png"
theme.titlebar_maximized_button_normal_active   = theme.dir .. "/icons/titlebar/maximized_normal_active.png"
theme.titlebar_maximized_button_focus_inactive  = theme.dir .. "/icons/titlebar/maximized_focus_inactive.png"
theme.titlebar_maximized_button_normal_inactive = theme.dir .. "/icons/titlebar/maximized_normal_inactive.png"

awful.util.tagnames   = { "WEB", "DEV", "SYS", "FUN" }

local markup     = lain.util.markup
local separators = lain.util.separators
local white      = theme.fg_focus
local gray       = "#858585"

local SailorBlue_Mint                 = {"#00203FFF","#ADEFD1FF"}
local Gray_LimePunch                  = {"#606060FF","#D6ED17FF"}
local ForestGreen_MossGreen           = {"#2C5F2D"  ,"#97BC62FF"}
local RoyalBlue_Peach                 = {"#00539CFF","#EEA47FFF"}
local ElectricBlueLemonade_Aquamarine = {"#0063B2FF","#9CC3D5FF"}
local Black_BlazingYellow             = {"#101820FF","#FEE715FF"}
local CopperCoin_AgedCopper           = {"#B1624EFF","#5CC8D7FF"}
local SkyBlue_White                   = {"#89ABE3FF","#FCF6F5FF"}
local DuskyCitron_CoolGray            = {"#E3CD81FF","#B1B3B3FF"}
local Black_Orange                    = {"#101820FF","#F2AA4CFF"}
local BrownSugar_Beige                = {"#A07855FF","#D4B996FF"}
local TurkishSea_Silver               = {"#195190FF","#A2A2A1FF"}
local RoyalPurple_IceFlow             = {"#603F83FF","#C7D3D4FF"}
local IslGreen_White                  = {"#2BAE66FF","#FCF6F5FF"}
local Black_CherryTomato              = {"#2D2926FF","#E94B3CFF"}
local MangoMojito_TerrariumMoss       = {"#DAA03DFF","#616247FF"}
local SpaceCherry_White               = {"#990011FF","#FCF6F5FF"}
local SweetCorn_Toffee                = {"#F2EDD7FF","#755139FF"}
local DarkGreen_Black                 = {"#006B38FF","#101820FF"}
local AspenGold_PrincessBlue          = {"#FFD662FF","#00539CFF"}
local Soybean_Eclipse                 = {"#D7C49EFF","#343148FF"}
local MellowYellow_VerdantGreen       = {"#FFE77AFF","#2C5F2DFF"}
local PowderedSugar_Silver            = {"#F1F4FFFF","#A2A2A1FF"}
local LemonTonic_Purple               = {"#FCF951FF","#422057FF"}
local DarkBlue_Red                    = {"#00239CFF","#E10600FF"}

local LivingCoral_StormGray_ForestBiome    = {"#FC766AFF","#B0B8B4FF","#184A45FF"}
local BlazingOrange_BuffOrange_YellowCream = {"#FFA351FF","#FFBE7BFF","#EED971FF"}
local SagebrushGreen_Marsala_GraniteGray   = {"#567572FF","#964F4CFF","#696667FF"}
local Red_NorseBlue_LightGreen             = {"#DA291CFF","#56A8CBFF","#53A567FF"}
local GrassGreen_LightestSky_Clearwater    = {"#7DB46CFF","#E7EBE0FF","#ABD6DFFF"}
local Red_Yellow_Navy                      = {"#F65058FF","#FBDE44FF","#28334AFF"}
local TanagerTurquoise_TealBlue_KellyGreen = {"#95DBE5FF","#078282FF","#339E66FF"}
local PuffinBill_Green_Brown               = {"#E95C20FF","#006747FF","#4F2C1DFF"}
local DangerRed_TapShoe_BlueBlossom        = {"#D9514EFF","#2A2B2DFF","#2DA8D8FF"}

local White_VanillaCustard_Goldfinch_ScarletSage = {"#FCF6F5FF","#F0E1B9FF","#F3DB74FF","#A13941FF"}
local DeepBlue_NorthernSky_BabyBlue_Coffee       = {"#2460A7FF","#85B3D1FF","#B3C7D6FF","#D9B48FFF"}
local HabaneroGold_Dijon_Honey_Chestnut          = {"#FFD653FF","#DDB65DFF","#EEB238FF","#6E4C1EFF"}
local DelphiniumBlue_White_Atmosphere_FieryCoral = {"#669DB3FF","#F0F6F7FF","#A89C94FF","#FF4F58FF"}
local DarkGreen_LightGreen_StarWhite_Red         = {"#0A5E2AFF","#6DAC4FFF","#EFEFE8FF","#FE0000FF"}
local BlueSky_Elation_Nugget_Celestial           = {"#ABD1C9FF","#DFDCE5FF","#DBB04AFF","#97B3D0FF"}
local colors1                                     = {"#36688D","#F3CD05","#F49F05","#F18904","#BDA589"}
local colors                                     = {"#192E5B","#1D65A6","#72A2C0","#A89C94FF","#F3CD05","#2D2926FF"} --F2A104 

 --F2A104-- Separators
local arrow = separators.arrow_left

--Another calendar 
local calendar_widget = require("awesome-wm-widgets.calendar-widget.calendar")
    -- ...
    -- Create a textclock widget
    local mytextclock = wibox.widget.textclock(markup(white, " %a")
    .. markup(white, " %d ") .. markup(white, "%b ") ..  markup(white, "%H:%M "))
    mytextclock.font = theme.font
    -- default
    local cw = calendar_widget()
    -- or customized
    local cw = calendar_widget({
        theme = 'nord',
        placement = 'top_right'
    })
    mytextclock:connect_signal("button::press",
      function(_, _, _, button)
          if button == 1 then cw.toggle() end
      end)

-- Weather
theme.weather = lain.widget.weather({
    city_id = 3688689, -- Bogotá
    notification_preset = { font = "Monospace 10" },
    settings = function()
        units = math.floor(weather_now["main"]["temp"])
        widget:set_markup(" " .. markup.font(theme.font, markup(white,units) .. markup(white,"°C")) .. " ")
    end
})

-- MEM
local memicon = wibox.widget.imagebox(theme.widget_mem)
local mem = lain.widget.mem({
    settings = function()
        widget:set_markup(markup.font(theme.font, " " .. mem_now.used .. "MB "))
    end
})

-- MEM
local memicon2 = wibox.widget.imagebox(theme.widget_mem)
local memory = lain.widget.mem({
    settings = function()
        widget:set_markup(markup.fontfg(theme.font, "#e0da37", mem_now.used .. "M "))
    end
})

-- CPU
local cpuicon = wibox.widget.imagebox(theme.widget_cpu)
local cpu = lain.widget.cpu({
    settings = function()
        widget:set_markup(markup.font(theme.font, " " .. markup(white,cpu_now.usage) .. markup(white,"% ")))
    end
})

local cpu_widget = require("themes.dremora.cpu-widget"){
    width = 70,
    step_width = 2,
    step_spacing = 0,
    color = '#434c5e',
    enable_kill_button = true
}

-- Separators
local first     = wibox.widget.textbox('<span font="Terminus 4"> </span>')
local arrl_pre  = separators.arrow_right("alpha", "#1A1A1A")
local arrl_post = separators.arrow_right("#1A1A1A", "alpha")

function theme.at_screen_connect(s)
    -- Quake application
    s.quake = lain.util.quake({ app = awful.util.terminal })
    --Autostart

awful.spawn.with_shell("picom")
awful.spawn.with_shell("nitrogen --restore")

    -- If wallpaper is a function, call it with the screen
    --local wallpaper = theme.wallpaper
    --if type(wallpaper) == "function" then
        --wallpaper = wallpaper(s)
    --end
    --gears.wallpaper.maximized(wallpaper, s, true)

    -- Tags
    awful.tag(awful.util.tagnames, s, awful.layout.layouts)

    -- Create a promptbox for each screen
    s.mypromptbox = awful.widget.prompt()
    -- Create an imagebox widget which will contains an icon indicating which layout we're using.
    -- We need one layoutbox per screen.
    s.mylayoutbox = awful.widget.layoutbox(s)
    s.mylayoutbox:buttons(my_table.join(
                           awful.button({}, 1, function () awful.layout.inc( 1) end),
                           awful.button({}, 2, function () awful.layout.set( awful.layout.layouts[1] ) end),
                           awful.button({}, 3, function () awful.layout.inc(-1) end),
                           awful.button({}, 4, function () awful.layout.inc( 1) end),
                           awful.button({}, 5, function () awful.layout.inc(-1) end)))
    -- Create a taglist widget
    s.mytaglist = awful.widget.taglist(s, awful.widget.taglist.filter.all, awful.util.taglist_buttons)

    -- Create a tasklist widget
    s.mytasklist = awful.widget.tasklist(s, awful.widget.tasklist.filter.currenttags, awful.util.tasklist_buttons)

    -- Create the wibox
    s.mywibox = awful.wibar({ position = "top", screen = s, height = dpi(18), bg = theme.bg_normal, fg = theme.fg_normal })

    -- Add widgets to the wibox
    s.mywibox:setup {
        layout = wibox.layout.align.horizontal,
        { -- Left widgets
            layout = wibox.layout.fixed.horizontal,
            first,
            s.mytaglist,
            arrl_pre,
            s.mylayoutbox,
            arrl_post,
            s.mypromptbox,
            first,
        },
        s.mytasklist, -- Middle widget
        { -- Right widgets
            layout = wibox.layout.fixed.horizontal,
            wibox.widget.systray(),
            first,
            arrow(colors[6], colors[5]),
            wibox.container.background(wibox.container.margin(wibox.widget { memicon, mem.widget, layout = wibox.layout.align.horizontal }, dpi(2), dpi(3)), colors[5]),
            arrow(colors[5], colors[4]),
            wibox.container.background(wibox.container.margin(wibox.widget { cpuicon, cpu.widget, layout = wibox.layout.align.horizontal }, dpi(3), dpi(4)), colors[4]),
            arrow(colors[4], colors[3]),
            wibox.container.background(wibox.container.margin(wibox.widget { nill, cpu_widget, layout = wibox.layout.align.horizontal }, dpi(3), dpi(3)), colors[3]),
            arrow(colors[3], colors[2]),
            wibox.container.background(wibox.container.margin(wibox.widget { theme.weather.icon, theme.weather, layout = wibox.layout.align.horizontal }, dpi(4), dpi(4)), colors[2]),
            arrow(colors[2], colors[1]),
            wibox.container.background(wibox.container.margin(mytextclock, dpi(4), dpi(8)), colors[1]),
            arrow(colors[1], "alpha"),
            
        },
    }
end

return theme
