#! /bin/bash

options="A. Poweroff\nB. Reboot\nC. Suspend\nE. End Session\n"
choosen=$(echo -e "$options" | dmenu -i -p "Session:_" -sb "#c8ccd6" -sf "#1f1f1f" -nb "#080808" -l 6) 
case "$choosen" in
	"A. Poweroff") poweroff ;;
	"B. Reboot") reboot ;;
	"C. Hibernate") systemctl hibernate ;;	# not enought swap space lol ok. enable if you want
	"C. Suspend") systemctl suspend ;;	
	"E. End Session") pkill -KILL -u $USER ;;
	*) "That is not a valid option"
esac
