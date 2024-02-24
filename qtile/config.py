import os
from colorsheet import *
from libqtile import qtile, bar, layout, widget, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.config import ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration, RectDecoration, PowerLineDecoration
from libqtile.backend.wayland import InputConfig

# -- / NEEDED / --
#    nerd fonts (not precisely necesary)
#        scripts found at scripts folder (obligatory)
#            colorsheet.py for colors (obligatory)
#                programs: ranger, btop, nitrogen, dmenu (optional)


# --- / VARIABLES / ---
terminal =      "st";  #guess_terminal()
main_col =      mountainfuji["accents"]["kori"]
main_font =     'GeistMonoNerdFont'; fn_size = 11
scripts_path =  f"{os.path.expanduser('~')}/.config/scripts"
dmenu_run =     f"dmenu_run -i -p 'dmenu: ' -sb {defs['coldwhite']} -sf {defs['text']} -nb {defs['term']} -l 6"
wallfile =	'~/Pictures/wallpapers/downtown.jpg'; RoundCorner = 8;
profilepic = 	'~/Pictures/profilepics/jimbo3-modified.png'

def rectdeco(hexcolor,corner=None): #kesekki iwa
	return RectDecoration(
		filled=True, colour=hexcolor,padding=5,
		radius=corner if corner is not None else 0)		

widget_list=[  
    widget.Image(
        filename=profilepic,
        margin= 7, decorations=[rectdeco(fujibg["tetsu"],RoundCorner)]
    ),
    widget.Clock(  
        foreground=defs["white"], 
        format="   󱨴 %Y/%b/%d %a   ",        
	font=main_font, fontsize=fn_size,
        decorations=[rectdeco(fujibg["kesseki"],RoundCorner)],
    ),
    widget.Clock(  
        foreground=defs["text"], 
        format="   󱦟 %H-%M   ",        
	font=main_font, fontsize=fn_size,
        decorations=[rectdeco(main_col,RoundCorner)],
    ),
    widget.GroupBox(  
        this_current_screen_border=main_col, 
	active=defs["white"], 
        highlight_method='text', 
        borderwidth=0, margin_x=11, padding=0,
        font=main_font, fontsize=(fn_size+1), 
        decorations=[rectdeco(fujibg["kesseki"],RoundCorner)],
    ),
    widget.Spacer(),
    widget.GenPollCommand(
        foreground=defs["white"], 
        font=main_font, fontsize=fn_size, 
        fmt = '  {}  ', shell=True,
        cmd= f'{scripts_path}/qtileblocks.sh battery',
        update_interval=60,
        decorations=[rectdeco(fujibg["kesseki"],RoundCorner)],
    ),
    widget.WidgetBox(
        fmt= '   {} ⠀  ', foreground=main_col, 
        text_closed='󰘸', text_open='󰘹', 
        close_button_location='right',
        widgets=[widget.Systray()], 
        font=main_font, fontsize=14, 
        decorations=[rectdeco(fujibg["tetsu"],RoundCorner)],
    ), 
]

# --- / MODKEYS / ---
MOD  = "mod4";      #WINDOWS KEY
ALT  = "mod1";      #ALT KEY
CTRL = "control";   #CONTROL KEY
SHIFT= "shift";     #SHIFT KEY

#autorun commands at start
autostart=[ 
    "setxkbmap -layout gb",
    #"setxkbmap gb dvorak",
    "xrdb -load ~/.Xresources",  
    "picom &", 
    "nm-applet &",
    "xset r rate 350 60",
];  
for command in autostart: 
    os.system(command)

groups = [
    ScratchPad('0',[
        DropDown(
        "files", f"{terminal} -e ranger", 
        x=0.251,    y=0.18,
        width=0.50, height=0.50,
        on_focus_lost_hide=False),

        DropDown(
        "wall", "nitrogen",
        x=0.49,    y=0.58,
        width=0.50, height=0.40,
        on_focus_lost_hide=False),

        DropDown(
        "btop", f"{terminal} -e htop",
        x=0.155,    y=0.11,
        width=0.70, height=0.70,
        on_focus_lost_hide=False),
    ]),

    Group('1',label=" ", matches=[Match(wm_class=["firefox"])]),
    Group('2',label="󰘳 ", matches=[Match(wm_class=["VSCodium"])], layout="spiral"), 
    Group('3',label=" ", matches=[Match(wm_class=[""])], layout="spiral"), 
    Group('4',label=" ", matches=[Match(wm_class=["spotify"])]),
    Group('5',label=" ", matches=[Match(wm_class=["discord"])]), 
    Group('6',label="󰊴 ", matches=[Match(wm_class=["Steam","steam",])]), 
    Group('7',label="󰍷 ", matches=[Match(wm_class=[""])]),
    Group('8',label="󰍷 ", matches=[Match(wm_class=[""])]),
    Group('9',label="󰍷 ", matches=[Match(wm_class=[""])]),

]

layouts = [
    layout.Bsp(
        border_on_single=1,
        border_width = 1,
        margin_on_single=10,
        margin=10,
        border_focus=defs["egg"],
        border_normal=defs["unused"],
        lower_right=False, 
    ), 
    layout.Spiral( 
        border_focus=defs["coldwhite"],
        border_normal=defs["unused"],
        border_width = 1, margin=10,
        main_pane='right', clockwise=True,
        new_client_position='left',
    ),

]

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
        Key([MOD], "h", lazy.layout.left(), desc="Move focus to left"),
        Key([MOD], "l", lazy.layout.right(), desc="Move focus to right"),
        Key([MOD], "j", lazy.layout.down(), desc="Move focus down"),
        Key([MOD], "k", lazy.layout.up(), desc="Move focus up"),
        Key([MOD], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
        Key([MOD, SHIFT], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
        Key([MOD, SHIFT], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
        Key([MOD, SHIFT], "j", lazy.layout.shuffle_down(), desc="Move window down"),
        Key([MOD, SHIFT], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
        Key([MOD, CTRL], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
        Key([MOD, CTRL], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
        Key([MOD, CTRL], "j", lazy.layout.grow_down(), desc="Grow window down"),
        Key([MOD, CTRL], "k", lazy.layout.grow_up(), desc="Grow window up"),
        Key([MOD, CTRL], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
        Key([MOD],"Return", lazy.layout.toggle_split(), desc="Toggle split/unsplit sides of stack",),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    #    multiple stack panes
 
    Key([MOD], "return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([MOD], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([MOD, CTRL], "r", lazy.reload_config(), desc="Reload the config"),
    Key([MOD, CTRL], "q", lazy.shutdown(), desc="Shutdown Qtile"), 
    
    #SCRATCHPADS & GROUPS
    Key([MOD], "Tab", lazy.screen.next_group(), desc="move to next layout"),
    Key([ALT], "Tab", lazy.screen.prev_group(), desc="move to previous layout"),
    Key([MOD, CTRL], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([MOD], "r", lazy.group['0'].dropdown_toggle('files')), 
    Key([MOD], "w", lazy.group['0'].dropdown_toggle('wall')), 
    Key([MOD], "b", lazy.group['0'].dropdown_toggle('btop')), 
    
    #SPAWN STUFFFF
    Key([MOD], "x", lazy.spawn(f"{scripts_path}/turnoff.sh"), desc="close up menu"),
    Key([MOD], "z", lazy.spawn(f"{scripts_path}/wifi.sh"), desc="wifi connection menu"),
    Key([MOD], "d", lazy.spawn(dmenu_run), desc="Execute programs with rofi"),
    Key([MOD], "s", lazy.spawn("flameshot gui"), desc="screenshot with flameshot"),
    Key([MOD, CTRL], "1", lazy.spawn("setxkbmap -layout gb"), desc="change layout to united kingdom qwerty"),
    Key([MOD, CTRL], "2", lazy.spawn("setxkbmap latam"), desc="change layout to latam qwerty"),
    Key([MOD, CTRL], "3", lazy.spawn("setxkbmap gb dvorak"), desc="change layout to gb dvorak"),
    
    #EXTRA FUNCTIONALITY 
    Key([MOD], "f", lazy.window.toggle_fullscreen(), desc="toggle fullscreen"), 
    Key([],"XF86AudioRaiseVolume",  lazy.spawn(f"{scripts_path}/vol_bri.sh volume_up"), desc="VOLUME UP"),
    Key([],"XF86AudioLowerVolume",  lazy.spawn(f"{scripts_path}/vol_bri.sh volume_down"), desc="VOLUME DOWN"),
    Key([],"XF86AudioMute",         lazy.spawn(f"{scripts_path}/vol_bri.sh volume_mute"), desc="VOLUME MUTE"),
    Key([],"XF86MonBrightnessUp",   lazy.spawn(f"{scripts_path}/vol_bri.sh brightness_up"), desc="BRIGHTNESS UP"),
    Key([],"XF86MonBrightnessDown", lazy.spawn(f"{scripts_path}/vol_bri.sh brightness_down"), desc="BRIGHTNESS DOWN"),
    Key([],"XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc="Player"),
    Key([],"XF86AudioNext", lazy.spawn("playerctl next"), desc="Player"),
    Key([],"XF86AudioPrev", lazy.spawn("playerctl previous"), desc="Player"),
    Key([],"XF86AudioStop", lazy.spawn("playerctl stop"), desc="Player"),
    
]


'''     List of commands in case vol_bri.sh is unavailable
        VOL+ = pactl set-sink-volume @DEFAULT_SINK@ +5%
        VOL- = pactl set-sink-volume @DEFAULT_SINK@ -5%
        MUTE = pactl set-sink-mute @DEFAULT_SINK@ toggle
        MIC-MUTE = pactl set-source-mute @DEFAULT_SOURCE@ toggle 
        BRI+ = brightnessctl set 5%+
        BRI- = brightnessctl set 5%-
        
        OG groups variable with workspaces as numbers
        groups = [Group(i) for i in "123456789"]
         
'''

for i in groups:
    keys.extend(
        [   Key([MOD], i.name, lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),       ),
            Key([MOD, SHIFT], i.name, lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),      ),
        ]
    )

widget_defaults = dict( font="sans", fontsize=12, padding=3, )
extension_defaults = widget_defaults.copy()


screens = [
    Screen(       
        wallpaper=wallfile,
        wallpaper_mode='stretch', 
        bottom=bar.Bar(
            widget_list,
            size=35, opacity=1,
            border_width=[0,0,0,0], #N E S W
            background=defs["term"], 
            #border_color = fujibg["tetsu"], 
            #margin=3, 
        ),      
        top = bar.Gap(5), 
        left= bar.Gap(10), 
        right= bar.Gap(10),
    ),
]


#Drag floating layouts.
mouse = [
    Drag ([MOD], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag ([MOD], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([MOD], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False


floating_layout = layout.Floating(
    border_focus=defs["coldwhite"],
    border_normal=defs["coldwhite"],
    border_width =1,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# WHY THIS DOES NOT WORK FOR ME HELP IM TIRED OF THIS
# i cannot run qtile on wayland, if you know how to contact me
'''
if qtile.core.name == "x11":
    term = "st"
elif qtile.core.name == "wayland":
    term = guess_terminal()

# Configure input devices
try: 
    wl_input_rules = {
        "type:keyboard": InputConfig(
            kb_layout='gb',
            kb_repeat_rate=60,
            kb_repeat_delay=350
        ),
    }
except ImportError:
    wl_input_rules = None
'''
# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
#wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
#wmname = "LG3D"
wmname = "QtileWM"

