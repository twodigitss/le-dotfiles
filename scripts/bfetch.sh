#! /bin/bash
# (\ /)  simpler
# ( . .)  fetch script
# c(*)(*)  written in pure bash by c:

C1='\033[0;41m'
C2='\033[0;42m'
C3='\033[0;43m'
C4='\033[0;44m'
C5='\033[0;45m'
C6='\033[0;46m'
CR='\033[1;31m'      # red
CM='\033[1;35m'      # magenta
CB='\033[1;36m'      # blue
CC='\033[0;37m'      # black/white
IT='\033[1m\033[3m'  # bold italic
esc='\e[0m'

echo
echo -e ${CR}"         <3         "${esc}${IT}'    os:'${esc} $OSTYPE
echo -e ${CC}"        /  \        "${esc}${IT}' shell:'${esc} $SHELL
echo -e ${CB}"  (\ /)   ${CM}  (\ (\  "${esc}${IT}'   term:'${esc} $TERM
echo -e ${CB}"  ( . .)  ${CM}  (. . ) "${esc}${IT}' editor:'${esc} $EDITOR
echo -e ${CB}"  c(*)(*) ${CM} (*)(*)o "${esc}${IT}'   cols:'${esc} ${C1}'  '${C2}'  '${C3}'  '${C4}'  '${C5}'  '${C6}'  '${esc}
echo