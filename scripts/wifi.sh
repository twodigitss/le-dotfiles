#! /bin/bash

#options="0. Wifi Sala\n1. Wifi Cuarto\n2. Wifi Escuela\n3. Wifi Sabados\n"
options="A. Living Room\nB. Bedroom\nC. School\nD. Saturdays\n"
choosen=$(echo -e "$options" | dmenu -i -p "Network:_" -sb "#c8ccd6" -sf "#1f1f1f" -nb "#080808" -l 6) 
case "$choosen" in
	"A. Living Room") nmcli dev wifi connect INFINITUM1BCC password Qp6Ee5Sp5b ;;
	"B. Bedroom") nmcli dev wifi connect RDeRouter password 1234567890 ;;
	"C. School") nmcli dev wifi connect UNIFI-ITSA ;;
	"D. Saturdays") nmcli dev wifi connect INFINITUM5987_2.4 password 7kHekay2r6  ;;	
	*) 		"That is not a valid option"
esac
