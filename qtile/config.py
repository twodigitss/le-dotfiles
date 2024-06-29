# what the hell happened and what made me to do this...
import os,re,sys
sys.path.append(f"{os.path.expanduser('~')}/.config/qtile/modules")

from variables import *
from workspaces import groups
from keybinds import keys, mouse
from screens import screens
from layouts import layouts, floating_layout

# -- / NEEDED / --
#    nerd fonts (not precisely necesary)
#        scripts found at scripts folder (obligatory)
#                programs: ranger, btop, nitrogen, dmenu (optional)

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

