import re
from libqtile.config import ScratchPad, DropDown, Key, Group, Match
from libqtile.lazy import lazy
from keybinds import keys
from variables import MOD, SHIFT, terminal

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

    Group('1',label=" ", matches=[Match(wm_class=re.compile(r"^(Firefox)$"))]),
    Group('2',label="󰘳 ", matches=[Match(wm_class=re.compile(r"^(Codium)$"))], layout="spiral"), 
    Group('3',label=" ", matches=[Match(wm_class=re.compile(r"^()$"))], layout="spiral"), 
    Group('4',label=" ", matches=[Match(wm_class=re.compile(r"^(spotify)$"))]),
    Group('5',label=" ", matches=[Match(wm_class=re.compile(r"^(discord)$"))]), 
    Group('6',label="󰊴 ", matches=[Match(wm_class=re.compile(r"^(steam)$"))]), 
    Group('7',label="󰍷 ", matches=[Match(wm_class=re.compile(r"^()$"))]),
    Group('8',label="󰍷 ", matches=[Match(wm_class=re.compile(r"^()$"))]),
    Group('9',label="󰍷 ", matches=[Match(wm_class=re.compile(r"^()$"))]),

]



for i in groups:
    keys.extend(
        [   Key([MOD], i.name, lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),       ),
            Key([MOD, SHIFT], i.name, lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),      ),
        ]
    )


