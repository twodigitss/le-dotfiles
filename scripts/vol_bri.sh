#!/bin/bash
# I AM NOT THE AUTHOR OF THIS FILE, I FOUND OUT THE FILE UPLOADED BY SOMEONE
# ELSE AT UNIXPORN SUBREDDIT AND I AM ONLY UPLOADING FOR BACKUP PURPOSES
#

# See README.md for usage instructions
bar_color="#CEB188"
max_volume=100

function get_volume { 
	pactl get-sink-volume @DEFAULT_SINK@ | grep -Po '[0-9]{1,3}(?=%)' | head -1; }
function get_mute { 
	pactl get-sink-mute @DEFAULT_SINK@ | grep -Po '(?<=Mute: )(yes|no)'; }
function get_brightness {
    	#xbackligtht | grep -Po '[0-9]{1,3}' | head -n 1 
    	brightnessctl | grep -oP '\d+(?=%)'; }

# Displays a volume notification using dunstify
function show_volume_notif {
    volume=$(get_volume)
    dunstify -t 1000 -r 2593 -u normal "$volume %    󱡏  " -h int:value:$volume -h string:hlcolor:$bar_color 
}

# Displays a brightness notification using dunstify
function show_brightness_notif {
    brightness=$(get_brightness)
    get_brightness_icon
    dunstify -t 1000 -r 2593 -u normal "$brightness %    󱣝  " -h int:value:$brightness -h string:hlcolor:$bar_color
}

# Main function - Takes user input, "volume_up", "volume_down", "brightness_up", or "brightness_down"
case $1 in
    volume_up)
    	# Unmutes and increases volume, then displays the notification
       	pactl set-sink-volume @DEFAULT_SINK@ +1%
    	show_volume_notif
    ;;

    volume_down)
    	# Raises volume and displays the notification
    	pactl set-sink-volume @DEFAULT_SINK@ -1%
    	show_volume_notif
    ;;

    volume_mute)
    	# Toggles mute and displays the notification
    	pactl set-sink-mute @DEFAULT_SINK@ toggle
    	show_volume_notif
    ;;

    brightness_up)
    	# Increases brightness and displays the notification
    	brightnessctl set 1%+ 
    	show_brightness_notif
    ;;

    brightness_down)
    	# Decreases brightness and displays the notification
    	brightnessctl set 1%-
    	show_brightness_notif
    ;;

esac
