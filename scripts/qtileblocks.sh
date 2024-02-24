#!/bin/bash
#QTILE BLOCKS THING WRITTEN BY twodigitss
white='\e[0;37m'; 	black='\e[0;30m';
red='\e[0;31m';		green='\e[0;32m';	
yellow='\e[0;33m';	blue='\e[0;34m';
purple='\e[0;35m';	cyan='\e[0;36m';

bgwhite='\e[0;30;47m'; 	bgblack='\e[0;37;40m';
bgred='\e[0;30;41m';	bggreen='\e[0;30;42m';	
bgyellow='\e[0;30;43m';	bgblue='\e[0;30;44m';
bgpurple='\e[0;30;45m';	bgcyan='\e[0;30;46m';

endcol='\e[0m';		bold='\e[1m';
uline='\e[4m';		italic='\e[3m';


batteryfull() {
	pwr=$(cat /sys/class/power_supply/BAT0/capacity);
	sts=$(cat /sys/class/power_supply/BAT0/status);	icon=""
	if [ "$pwr" -ge 90 ]; then icon="󰁹";
	elif [ "$pwr" -lt 90 ] && [ "$pwr" -ge 80 ]; then icon="󰂂";
	elif [ "$pwr" -lt 80 ] && [ "$pwr" -ge 70 ]; then icon="󰂁";
	elif [ "$pwr" -lt 70 ] && [ "$pwr" -ge 60 ]; then icon="󰂀";
	elif [ "$pwr" -lt 60 ] && [ "$pwr" -ge 50 ]; then icon="󰁿";
	elif [ "$pwr" -lt 50 ] && [ "$pwr" -ge 40 ]; then icon="󰁾";
	elif [ "$pwr" -lt 40 ] && [ "$pwr" -ge 30 ]; then icon="󰁽";
	elif [ "$pwr" -lt 30 ] && [ "$pwr" -ge 20 ]; then icon="󰁼";
	elif [ "$pwr" -lt 20 ] && [ "$pwr" -ge 10 ]; then icon="󰁻";
	elif [ "$pwr" -lt 10 ] && [ "$pwr" -ge 0 ];  then icon="󰁺";
	fi	
	case "$sts" in
		"Charging") pwr="󱐋 $pwr%";;
		"Discharging") pwr="$pwr%" ;;  *) pwr="?$pwr%" ;;
	esac;
	echo -e "$icon $pwr"; }

batteryicon() {
	pwr=$(cat /sys/class/power_supply/BAT0/capacity);
	if [ "$pwr" -ge 90 ]; then icon="󰁹";
	elif [ "$pwr" -lt 90 ] && [ "$pwr" -ge 80 ]; then icon="󰂂";
	elif [ "$pwr" -lt 80 ] && [ "$pwr" -ge 70 ]; then icon="󰂁";
	elif [ "$pwr" -lt 70 ] && [ "$pwr" -ge 60 ]; then icon="󰂀";
	elif [ "$pwr" -lt 60 ] && [ "$pwr" -ge 50 ]; then icon="󰁿";
	elif [ "$pwr" -lt 50 ] && [ "$pwr" -ge 40 ]; then icon="󰁾";
	elif [ "$pwr" -lt 40 ] && [ "$pwr" -ge 30 ]; then icon="󰁽";
	elif [ "$pwr" -lt 30 ] && [ "$pwr" -ge 20 ]; then icon="󰁼";
	elif [ "$pwr" -lt 20 ] && [ "$pwr" -ge 10 ]; then icon="󰁻";
	elif [ "$pwr" -lt 10 ] && [ "$pwr" -ge 0 ];  then icon="󰁺";
	fi	
	echo -e "$icon"; }


batterynum() {
	pwr=$(cat /sys/class/power_supply/BAT0/capacity);
	sts=$(cat /sys/class/power_supply/BAT0/status);	icon=""
	case "$sts" in
		"Charging") pwr="> $pwr%";;
		"Discharging") pwr="$pwr%" ;;  *) pwr="?$pwr%" ;;
	esac;
	echo -e "$pwr"; }

volume() {
	vol="$(pactl list sinks | awk '/Volume:/{print $5; exit}' | tr -d '%')"
	if [ "$vol" -ge 40 ]; then echo -e "󰕾 $vol";
	elif [ "$vol" -lt 40 ] && [ "$vol" -ge 20 ]; then echo -e "󰖀 $vol";
	elif [ "$vol" -lt 20 ]; then echo -e "󰕿 $vol";
	fi }

brightness() {
	bgt="$(brightnessctl | grep -oP '\d+(?=%)')"
	echo -e "󰌶 $bgt%"; }

brightnessnum() {
	bgt="$(brightnessctl | grep -oP '\d+(?=%)')"
	echo -e "$bgt%"; }

clock() {
	dte="$(date +"%A   󱨰  %d/%b  󰔛  %H-%M"| sed 's/  / /g')"
	echo -e "$dte"; }

network(){
	ssid="$(iw dev | awk '/ssid/{print $2}')"; icon=" "
	signal=$(nmcli -t -f SIGNAL device wifi | head -n1 )
	case "$ssid" in
		"")ssid=" NULL ";;  
		*) ssid=" $ssid";;
	esac;
	if [ "$signal" = "--" ] || [ -z "$signal" ]; then icon="󰣽"
    	else
		#Categorize signal strength
		if [ "$signal" -ge 80 ]; then icon="󰣺";
		elif [ "$signal" -ge 60 ] && [ "$signal" -lt 80 ]; then icon="󰣸";
		elif [ "$signal" -ge 40 ] && [ "$signal" -lt 60 ]; then icon="󰣶";
		elif [ "$signal" -ge 20 ] && [ "$signal" -lt 40 ]; then icon="󰣴";
	    	else icon="󰣾";
		fi
	fi
	echo -e "$icon⠀$ssid";
	}

networkicon(){
	signal=$(nmcli -t -f SIGNAL device wifi | head -n1 )
	if [ "$signal" = "--" ] || [ -z "$signal" ]; then icon="󰣽"
    	else
		#Categorize signal strength
		if [ "$signal" -ge 80 ]; then icon="󰣺";
		elif [ "$signal" -ge 60 ] && [ "$signal" -lt 80 ]; then icon="󰣸";
		elif [ "$signal" -ge 40 ] && [ "$signal" -lt 60 ]; then icon="󰣶";
		elif [ "$signal" -ge 20 ] && [ "$signal" -lt 40 ]; then icon="󰣴";
	    	else icon="󰣾";
		fi
	fi
	echo -e "$icon";
	}

networkname(){
	ssid="$(iw dev | awk '/ssid/{print $2}')"; icon=" "
	case "$ssid" in
		"")ssid=" NULL ";;  
		*) ssid=" $ssid";;
	esac;
	echo -e "$ssid";
	}

keyboard(){
	kb=$(setxkbmap -query | awk '/layout/ {print $2}')
	case "$kb" in
		"gb") kb="Uk";; 	"us") kb="Us";;
		"latam") kb="Es";;	*) kb=$kb;;
	esac;
	echo -e "󱋷 :$kb"; }

updates(){ 
	upd=$(checkupdates | wc -l) 
	echo -e "󰄠 $upd"; }

cpu(){
	cpu=$(top -b -n1 | awk '/%Cpu/{print $2 + $4 "%"}')
	echo -e "  $cpu"; }

ram(){
	ram=$(free -m | awk '/Mem/ {print $3 " MB"}')
	echo -e "󰠘 $ram"; }

#THIS ONES ARE PARAMETER TO ADD THAT YOU WANT TO BE SHOWN
case $1 in
	battery)echo -e "$(batteryfull)";;
	batteryicon)echo -e "$(batteryicon)";;
	batterynum)echo -e "$(batterynum)";;
	volume)echo -e "$(volume)";;
	brightness) echo -e "$(brightness)" ;;
	brightnessnum) echo -e "$(brightnessnum)" ;;
	clock)echo -e "$(clock)";;
	network)echo -e "$(network)";;
	networkicon)echo -e "$(networkicon)";;
	networkname)echo -e "$(networkname)";;
	keyboard)echo -e "$(keyboard)";;
	updates)echo -e "$(updates)";;
	cpu)echo -e "$(cpu)";;
	ram)echo -e "$(ram)";;
esac


