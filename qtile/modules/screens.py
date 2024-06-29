from libqtile.config import Screen
from libqtile import bar
from variables import wallfile, widget_list
from colorsheet import defs, fujibg

screens = [
    Screen(       
        wallpaper = wallfile,
        wallpaper_mode = 'stretch', 
        bottom = bar.Bar(
            widget_list,
            size=35, opacity=1,
            border_width=[0,0,0,0], #N E S W
            background=defs["term"], 
            border_color = fujibg["fuyu"], 
            margin=5, 
        ),
        top = bar.Gap(10), 
        left = bar.Gap(10), 
        right = bar.Gap(10), 
    ),
]

