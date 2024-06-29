import sys,os 
from libqtile.lazy import lazy
from libqtile.config import Drag, Click, Key, ScratchPad, DropDown
from variables import MOD, ALT, CTRL, SHIFT, terminal, scripts_path, dmenu_run

# --- / ACTUAL KEYS / ---
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
    Key([MOD], "p", lazy.spawn(f"{scripts_path}/screenshots.sh"), desc="does screenshots"),
    Key([MOD], "d", lazy.spawn(dmenu_run), desc="Execute programs with Dmenu"),
    Key([MOD], "s", lazy.spawn("flameshot gui"), desc="screenshot with flameshot"),
    Key([MOD, CTRL], "1", lazy.spawn("setxkbmap -layout gb"), desc="change layout to united kingdom qwerty"),
    Key([MOD, CTRL], "2", lazy.spawn("setxkbmap gb dvorak"), desc="change layout to gb dvorak"),
    
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

#Drag floating layouts.
mouse = [
    Drag ([MOD], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag ([MOD], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([MOD], "Button2", lazy.window.bring_to_front()),
]


