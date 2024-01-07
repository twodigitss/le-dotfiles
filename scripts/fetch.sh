#!/bin/bash
# /--- COLORS !!! ---/
whit='\e[0;37m'; 	black='\e[0;30m'
gray='\e[0;30m';	red='\e[0;31m'
gree='\e[0;32m';	brown='\e[0;33m'
yell='\e[0;33m';	blue='\e[0;34m'
purp='\e[0;35m';	cyan='\e[0;36m'
end='\e[0m';		bold='\e[1m'
uline='\e[4m';		italic='\e[3m'

	B1='\033[0;41m  \e[0m \033[0;31m $1 \e[0m'; B2='\033[0;42m  \e[0m \033[0;32m $1 \e[0m'
	B3='\033[0;43m  \e[0m \033[0;33m $1 \e[0m'; B4='\033[0;44m  \e[0m \033[0;34m $1 \e[0m'
	B5='\033[0;45m  \e[0m \033[0;35m $1 \e[0m'; B6='\033[0;46m  \e[0m \033[0;36m $1 \e[0m'
	B7='\033[0;47m  \e[0m \033[0;37m $1 \e[0m'

# /--- VARIABLES ---/
OS=$(grep '^NAME=' /etc/os-release | awk -F '=' '{print $2}' | tr -d '"')
PKS=$(pacman -Qq | wc -l)
HDW=$(cat /sys/class/dmi/id/product_name)
CPU=$(lscpu | awk '/Model name/ {print $3, $4, $5, $6}')
GPU=$(lspci | grep -iE "VGA|3D|Display" | awk -F '[:[:space:]]+' '{print $6,$7,$8,$9,$10}')

USR=$(whoami)
HST=$(hostname)
KNL=$(uname -r)
UPT=$(uptime | awk -F'[ ,]+' '{print $4, "minutes"}')
WM=$(echo $XDG_SESSION_DESKTOP)
SH=$(echo $SHELL)

# 4,5,2,3,6,1,7
echo -e "   ${C4}  ${end} ${blue}	OS${end}: $OS"
echo -e "   ${C5}  ${end} ${purp}	Host${end}: $HST"
echo -e "   ${C2}  ${end} ${gree}	WM${end}: $WM ${gree} shell${end}: $SH"
echo -e "   ${C3}  ${end} ${yell}	Kernel${end}: $KNL"
echo -e "   ${C6}  ${end} ${cyan}	Packages${end}: $PKS ${italic}(pacman)${end}"
echo -e "   ${C1}  ${end} ${red}	Uptime${end}: $UPT"
echo -e "   ${C7}  ${end} ${white}	Hardware${end}: $CPU"
echo ""




