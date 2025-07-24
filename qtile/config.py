#MY BEAUTIFUL DOTFILES!!! TOO MUCH ENGINEERING
from os import system, path, listdir
from colorsheet import themes, catpuccin, biscuit, defs
from random import choice
from libqtile import layout, bar
from libqtile.config import ScratchPad, DropDown, Key, Group, Match, Drag, Click, Key, ScratchPad, DropDown, Screen
from libqtile.utils import guess_terminal
from libqtile.lazy import lazy
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration; #PowerLineDecoration, BorderDecoration
from libqtile.backend.wayland import InputConfig

# -- / NEEDED / --
#    nerd fonts (not precisely neccesary)
#        scripts found at scripts folder (obligatory)
#           qtile_extras package installed (neccesary)


##################################################################
###                       THEME CLASS                          ###
##################################################################

#from qtile_extras.widget.decorations import RectDecoration; #PowerLineDecoration, BorderDecoration
#from random import choice

wallDir = "/home/gwyne/Pictures/wallpapers/"

# --- / SOME FUNCTIONS THAT HELPS MY LAZYNESS / ---
def RD(hex,corner=None) -> object: 
	return RectDecoration( 
	    radius = 0 if corner is None else corner,
        filled = True, colour = hex, padding = 4, )

#TO RANDOMIZE WALLPAPERS IF IM TOO BORED
def randomWall(directory = wallDir) -> str:
    files = listdir(directory); image_extensions = ('.jpg', '.png')
    wallpapers = [f for f in files if path.splitext(f)[1].lower() in image_extensions]
    if not wallpapers: return None
    random_wallpaper = choice(wallpapers)
    return directory + random_wallpaper

#SETS THEME (:
class Theme:
    def __init__(self, theme_name) -> object:
        self.name = theme_name
        self.bgAlpha = "#00000000"
        self.themes = {
            'dark': {
                'main':     catpuccin['frappe']['Blue'],
                'textAlt':  themes['light']['text'],
                'text':     themes['dark']['text'],
                'bg1':      themes['dark']["kesseki"],
                'bg2':      themes['dark']["iwa"],
            },
            'light': {
                'main':     biscuit['light']['ChineseViolet'],
                'textAlt':  themes['dark']['text'],
                'text':     themes['light']['text'],
                'bg1':      themes['light']["term"],
                'bg2':      themes['light']["bg1"],
            }
        }
        self.set_theme(theme_name)
    
    #DECLARES VARIABLES ACORDING TO THEME
    def set_theme(self, theme_name) -> None:
        if theme_name not in self.themes:
            raise ValueError("Invalid theme name")
        
        theme = self.themes[theme_name]
        self.main = theme['main']
        self.textCol = theme['text']
        self.textColAlt = theme['textAlt']
        self.bg1 = theme['bg1']
        self.bg2 = theme['bg2']


##################################################################
###                       VARIABLES			    			   	###
##################################################################

#from libqtile.utils import guess_terminal

# --- / VARIABLES / ---
radius = 8 ; 
fn_size = 10
theme =	Theme("dark")
terminal = "warp-terminal" or guess_terminal(); 
main_font = "MapleMono"; 
scripts_path = "/home/gwyne/.config/scripts"
wallfile = randomWall(); #f"{wallDir}/prometheus_upscaled2.png";

# --- / MODKEYS / ---
MOD  = "mod4";      #WINDOWS KEY
ALT  = "mod1";      #ALT KEY
CTRL = "control";   #CONTROL KEY
SHIFT= "shift";     #SHIFT KEY


##################################################################
###                         WIDGETS                            ###
##################################################################

#from libqtile.lazy import lazy
#from qtile_extras import widget

# --- / WIDGETS / ---
widget_list=[
    widget.GroupBox(  
        this_current_screen_border=theme.main, 
	    active=theme.textCol, inactive='#818181',
        highlight_method='text', 
        borderwidth=0, margin_x=11, padding=0,
        font=main_font, fontsize=(fn_size), 
        visible_groups=["1","2","3","4","5"],
    ),
    widget.Prompt(
        font=main_font, 
        fontsize=fn_size,
    ),
    widget.Spacer(),
    #BATTERY
    widget.GenPollCommand(
        foreground=theme.textCol, 
        font=main_font, fontsize=fn_size, 
        fmt = '  {}  ', shell=True,
        cmd= "upower -i /org/freedesktop/UPower/devices/battery_BAT0 | awk '/state/ {s=$2} /percentage/ {p=$2} END {print s, p}'",
        update_interval=60,
    ),
    widget.Clock(  
        foreground=theme.textCol, 
        format="   %A  󱨰 %d/%b  󰦖 %H-%M   ",
        font=main_font, fontsize=fn_size,
    ),
    widget.QuickExit(
        foreground=theme.textCol, 
        default_text = "shutdown",
        font=main_font, fontsize=fn_size,
        countdown_format='  [{}]  ',
        fmt = "{}   ",
    ),
]


##################################################################
###                    GROUPS/WORKSPACES                       ###
##################################################################

#from libqtile.config import ScratchPad, DropDown, Key, Group, Match
#from libqtile.lazy import lazy

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

    Group('1', matches=[Match(wm_class="firefox")], layout="spiral"),
    Group('2', matches=[Match(wm_class="VSCodium")], layout="spiral"), 
    Group('3', matches=[Match(wm_class="")], layout="spiral"), 
    Group('4', matches=[Match(wm_class="spotify")]),
    Group('5', matches=[Match(wm_class="discord")]), 
    Group('6', matches=[Match(wm_class="steam")]), 
    Group('7', matches=[Match(wm_class="")]),
    Group('8', matches=[Match(wm_class="")]),
    Group('9', matches=[Match(wm_class="")]),

]


##################################################################
###                         LAYOUTS                            ###
##################################################################

#from libqtile import layout
#from libqtile.config import Match

layouts = [
    layout.Bsp(
        border_on_single=1,
        border_width = 0,
        margin_on_single=10,
        margin=5,
        border_focus=defs["egg"],
        border_normal=defs["unused"],
        lower_right=False, 
    ), 
    layout.Spiral( 
        border_focus=defs["coldwhite"],
        border_normal=defs["unused"],
        border_width = 0, margin=10,
        main_pane='right', clockwise=True,
        new_client_position='left',
    ),

]

floating_layout = layout.Floating(
    border_focus=defs["coldwhite"],
    border_normal=defs["coldwhite"],
    border_width = 0,
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


##################################################################
###                         KEYBINDS                           ###
##################################################################

#from libqtile.lazy import lazy
#from libqtile.config import Drag, Click, Key, ScratchPad, DropDown

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

# --- / ACTUAL KEYS / ---
keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
        Key([MOD], "h", lazy.layout.left(), desc="Move focus to left"),
        Key([MOD], "l", lazy.layout.right(), desc="Move focus to right"),
        Key([MOD], "j", lazy.layout.down(), desc="Move focus down"),
        Key([MOD], "k", lazy.layout.up(), desc="Move focus up"),
        # Key([MOD], "space", lazy.layout.next(), desc="Move window focus to other window"),
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
        # Key([MOD],"Return", lazy.layout.toggle_split(), desc="Toggle split/unsplit sides of stack",),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    #    multiple stack panes
 
    Key([MOD], "return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([MOD], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([MOD], "d", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([MOD, CTRL], "r", lazy.reload_config(), desc="Reload the config"),
    Key([MOD, CTRL], "q", lazy.shutdown(), desc="Shutdown Qtile"), 
    
    #SCRATCHPADS & GROUPS
    Key([MOD], "Tab", lazy.screen.next_group(), desc="move to next layout"),
    Key([ALT], "Tab", lazy.screen.prev_group(), desc="move to previous layout"),
    Key([MOD, CTRL], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    # Key([MOD], "r", lazy.group['0'].dropdown_toggle('files')), 
    # Key([MOD], "w", lazy.group['0'].dropdown_toggle('wall')), 
    # Key([MOD], "b", lazy.group['0'].dropdown_toggle('btop')), 
    
    #SPAWN STUFFFF
    # Key([MOD], "x", lazy.spawn(f"{scripts_path}/turnoff.sh"), desc="close up menu"),
    # Key([MOD], "z", lazy.spawn(f"{scripts_path}/wifi.sh"), desc="wifi connection menu"),
    # Key([MOD], "d", lazy.spawn(dmenu_run), desc="Execute programs with Dmenu"),
    #Key([MOD], "d", lazy.spawn("ulauncher"), desc="Execute programs with ULauncher"),
    # Key([MOD], "p", lazy.spawn(f"{scripts_path}/screenshots.sh"), desc="does screenshots"),
    # Key([MOD], "s", lazy.spawn("flameshot gui"), desc="screenshot with flameshot"),
    # Key([MOD, CTRL], "1", lazy.spawn("setxkbmap -layout gb"), desc="change layout to united kingdom qwerty"),
    # Key([MOD, CTRL], "2", lazy.spawn("setxkbmap gb dvorak"), desc="change layout to gb dvorak"),
    
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

#Drag floating layouts.
mouse = [
    Drag ([MOD], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag ([MOD], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([MOD], "Button2", lazy.window.bring_to_front()),
]

for i in groups:
    keys.extend(
        [   Key([MOD], i.name, lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),       ),
            Key([MOD, SHIFT], i.name, lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),      ),
        ]
    )


##################################################################
###                       SCREENS/BAR                          ###
##################################################################

#from libqtile.config import Screen
#from libqtile import bar

barPos = "top"

MyBar = bar.Bar(
    widget_list,
    # background = '#00000040',
    size = 30 if barPos=='top' else 33, 
    opacity = 1,
    #margin=[5,5,5,5],
    #border_width = [1,1,1,1],
    #border_color = '',
)

screens = [
    Screen(       
        wallpaper = wallfile,
        wallpaper_mode = 'stretch', 
        top = 	  MyBar if barPos=="top"     else bar.Gap(00), 
        left = 	  MyBar if barPos=="left"    else bar.Gap(00), 
        right =   MyBar if barPos=="right"   else bar.Gap(00), 
        bottom =  MyBar if barPos=="bottom"  else bar.Gap(00),
    ),
]


##################################################################
###                       ✨ ELSE ✨                           ###
##################################################################

#autorun commands at start
autostart=[ 
    # "setxkbmap -layout gb",
    "nm-applet &",
    "picom &",
    "xset r rate 350 60",
];  

# for command in autostart: 
#     system(command)

wl_input_rules = {
    # "type:pointer": InputConfig(tap=True),
    # Activa tap-to-click para tu touchpad (se detecta como un pointer)
    "1267:12447:ELAN1200:00 04F3:309F Touchpad": InputConfig(
        tap=True,
        click_method="clickfinger",         # o "button_areas" si prefieres
        natural_scroll=True                  # opcional: scroll natural
    ),
    # Ajusta la repetición del teclado
    "type:keyboard": InputConfig(
        kb_repeat_delay=350,                # delay en ms antes de repetir
        kb_repeat_rate=60                   # repeticiones por segundo
    ),
    # "1267:12377:ELAN1300:00 04F3:3059 Touchpad": InputConfig(left_handed=True),
    # "*": InputConfig(tap: True, left_handed=True, pointer_accel=True),
    # "type:keyboard": InputConfig(kb_options="ctrl:nocaps,compose:ralt"),
}

widget_defaults = dict( font="sans", fontsize=12, padding=3, )
extension_defaults = widget_defaults.copy()

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

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

