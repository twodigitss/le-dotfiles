from os import system, path
from qtile_extras import widget
from libqtile.utils import guess_terminal
from colorsheet import defs, mountainfuji, fujibg
from qtile_extras.widget.decorations import BorderDecoration, RectDecoration, PowerLineDecoration

# --- / VARIABLES / ---
terminal =      "st"; #guess_terminal()
profilepic = 	'~/Pictures/pics/wife.png'
main_font =     'CousineNerdFont'; fn_size = 12
scripts_path =  f"{path.expanduser('~')}/.config/scripts"
wallfile =	    '~/Pictures/wallpapers/COTN.png'; radius = 8;
dmenu_run =     f"dmenu_run -i -p 'dmenu: ' -sb {defs['coldwhite']} -sf {defs['text']} -nb {defs['term']} -l 0"

main_col =      mountainfuji["accents"]["ajisai"]
bg1 = fujibg["kesseki"]; bg2 = fujibg["iwa"]; 

# --- / MODKEYS / ---
MOD  = "mod4";      #WINDOWS KEY
ALT  = "mod1";      #ALT KEY
CTRL = "control";   #CONTROL KEY
SHIFT= "shift";     #SHIFT KEY

# --- / SOME WIDGETS CONFIGURATION / ---
def rectdeco(hexcolor,corner=None): #kesekki iwa
	return RectDecoration(
		filled=True, colour=hexcolor,padding=5,
		radius=corner if corner is not None else 0)		

widget_list=[  
    widget.Image(
        filename=profilepic,
        margin= 7, 
        decorations=[rectdeco(bg2,10)]
    ),
    widget.KeyboardLayout(
        fmt = '  {}  ',   
        foreground=main_col,
        font=main_font, fontsize=fn_size,
        configured_keyboards=['gb','us','latam'],
        decorations=[rectdeco(bg2,radius)]
    ),
    widget.CurrentLayout(
        fmt='     {}    ',
        font=main_font, fontsize=fn_size,    
        foreground=defs["text"],
        decorations=[rectdeco(main_col,radius)]
    ), 
    widget.GroupBox(  
        this_current_screen_border=main_col, 
	    active=defs["white"], 
        highlight_method='text', 
        borderwidth=0, margin_x=11, padding=0,
        font=main_font, fontsize=(fn_size+0), 
        visible_groups=["1","2","3","4","5","6"],
        decorations=[rectdeco(bg1,radius)]
    ),
    #BATTERY
    widget.GenPollCommand(
        foreground=defs["white"], 
        font=main_font, fontsize=fn_size, 
        fmt = '  {}  ', shell=True,
        cmd= f'{scripts_path}/qtileblocks.py battery',
        update_interval=60,
        decorations=[rectdeco(bg1,radius)]
    ),
    widget.Spacer(),
    widget.GenPollCommand(
        foreground=defs["white"], 
        font=main_font, fontsize=fn_size, 
        fmt = '  {}  ', shell=True,
        cmd= f'{scripts_path}/qtileblocks.py brightness',
        update_interval=60,
        decorations=[rectdeco(bg2,radius)]
    ),
    widget.Volume(  
        fmt = '  󱡏  {}   ',  
        font=main_font, fontsize=fn_size, 
        foreground=main_col, 
        decorations=[rectdeco(bg1,radius)]
    ), 
    widget.Spacer(),
    widget.WidgetBox(
        fmt= '   {} ⠀  ', foreground=defs["text"], 
        text_closed='󰘸', text_open='󰘹', 
        close_button_location='right',
        widgets=[widget.Systray()], 
        font=main_font, fontsize=14, 
        decorations=[rectdeco(main_col,radius)],
    ), 
    widget.Clock(  
        foreground=defs["coldwhite"], 
        format="   %A  󱨰 %d/%b  󰦖 %H-%M   ", #old format: %d%m%y 
        font=main_font, fontsize=fn_size,
        decorations=[rectdeco(bg1,radius)]
    ),
    widget.GenPollCommand(
        foreground=defs["coldwhite"], 
        font=main_font, fontsize=fn_size, 
        fmt = '  {}  ', shell=True,
        cmd= f'{scripts_path}/qtileblocks.py network',
        update_interval=60,
        decorations=[rectdeco(bg1,radius)]
    ),
    widget.TextBox(
        "     ", foreground=main_col,
        font=main_font, fontsize=fn_size,
        decorations=[rectdeco(bg2,radius)]
    ),
]

#autorun commands at start
autostart=[ 
    "setxkbmap -layout gb",
    "nm-applet &",
    "picom &",
    "xset r rate 350 60",
];  

for command in autostart: 
    system(command)

