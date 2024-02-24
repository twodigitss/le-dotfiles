#!/bin/bash
# I AM NOT THE AUTHOR OF THIS FILE, I FOUND OUT THE FILE UPLOADED BY SOMEONE
# ELSE AT UNIXPORN SUBREDDIT AND I AM ONLY UPLOADING FOR BACKUP PURPOSES
#

# See README.md for usage instructions
bar_color="#c8ccd6"
volume_step=1
brightness_step=1
max_volume=200


function get_volume { 
	pactl get-sink-volume @DEFAULT_SINK@ | grep -Po '[0-9]{1,3}(?=%)' | head -1; }
function get_mute { 
	pactl get-sink-mute @DEFAULT_SINK@ | grep -Po '(?<=Mute: )(yes|no)'; }
function get_brightness {
    	#xbackligtht | grep -Po '[0-9]{1,3}' | head -n 1 
    	brightnessctl | grep -oP '\d+(?=%)'; }

function get_brightness_icon { 
	brightness_icon="󱟇  : "; }

function get_volume_icon {
    volume=$(get_volume)
    mute=$(get_mute)
    if [ "$volume" -eq 0 ] || [ "$mute" == "yes" ] ; then
        volume_icon="󰩅  : "
    elif [ "$volume" -lt 30 ]; then
        volume_icon="󰟅  : "
    elif [ "$volume" -lt 70 ]; then
        volume_icon="󰟅  : "
    else
        volume_icon="󰟅  : "
    fi; }

# Displays a volume notification using dunstify
function show_volume_notif {
    volume=$(get_mute)
    get_volume_icon
    dunstify -t 1000 -r 2593 -u normal "$volume_icon $volume" -h int:value:$volume -h string:hlcolor:$bar_color 
}

# Displays a brightness notification using dunstify
function show_brightness_notif {
    brightness=$(get_brightness)
    get_brightness_icon
    dunstify -t 1000 -r 2593 -u normal "$brightness_icon $brightness" -h int:value:$brightness -h string:hlcolor:$bar_color
}

# Main function - Takes user input, "volume_up", "volume_down", "brightness_up", or "brightness_down"
case $1 in
    volume_up)
    	# Unmutes and increases volume, then displays the notification
    	pactl set-sink-mute @DEFAULT_SINK@ 0
    	volume=$(get_volume)
    	if [ $(( "$volume" + "$volume_step" )) -gt $max_volume ]; then
        	pactl set-sink-volume @DEFAULT_SINK@ $max_volume%
    	else
        	pactl set-sink-volume @DEFAULT_SINK@ +$volume_step%
    	fi
    	show_volume_notif
    ;;

    volume_down)
    	# Raises volume and displays the notification
    	pactl set-sink-volume @DEFAULT_SINK@ -$volume_step%
    	show_volume_notif
    ;;

    volume_mute)
    	# Toggles mute and displays the notification
    	pactl set-sink-mute @DEFAULT_SINK@ toggle
    	show_volume_notif
    ;;

    brightness_up)
    	# Increases brightness and displays the notification
    	brightnessctl set $brightness_step%+ 
    	show_brightness_notif
    ;;

    brightness_down)
    	# Decreases brightness and displays the notification
    	brightnessctl set $brightness_step%-
    	show_brightness_notif
    ;;

esac
