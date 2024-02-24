#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

[[ -f ~/.welcome_screen ]] && . ~/.welcome_screen

_set_liveuser_PS1() {
    PS1='[\u@\h \W]\$ '
    if [ "$(whoami)" = "liveuser" ] ; then
        local iso_version="$(grep ^VERSION= /usr/lib/endeavouros-release 2>/dev/null | cut -d '=' -f 2)"
        if [ -n "$iso_version" ] ; then
            local prefix="eos-"
            local iso_info="$prefix$iso_version"
            PS1="[\u@$iso_info \W]\$ "
        fi
    fi
}
_set_liveuser_PS1
unset -f _set_liveuser_PS1

ShowInstallerIsoInfo() {
    local file=/usr/lib/endeavouros-release
    if [ -r $file ] ; then
        cat $file
    else
        echo "Sorry, installer ISO info is not available." >&2
    fi
}

[[ "$(whoami)" = "root" ]] && return

[[ -z "$FUNCNEST" ]] && export FUNCNEST=100          # limits recursive functions, see 'man bash'

## Use the up and down arrow keys for finding a command in history
## (you can write some initial letters of the command first).
bind '"\e[A":history-search-backward'
bind '"\e[B":history-search-forward'

################################################################################
## Some generally useful functions.
## Consider uncommenting aliases below to start using these functions.
##
## October 2021: removed many obsolete functions. If you still need them, please look at
## https://github.com/EndeavourOS-archive/EndeavourOS-archiso/raw/master/airootfs/etc/skel/.bashrc

_open_files_for_editing() {
    # Open any given document file(s) for editing (or just viewing).
    # Note1:
    #    - Do not use for executable files!
    # Note2:
    #    - Uses 'mime' bindings, so you may need to use
    #      e.g. a file manager to make proper file bindings.

    if [ -x /usr/bin/exo-open ] ; then
        echo "exo-open $@" >&2
        setsid exo-open "$@" >& /dev/null
        return
    fi
    if [ -x /usr/bin/xdg-open ] ; then
        for file in "$@" ; do
            echo "xdg-open $file" >&2
            setsid xdg-open "$file" >& /dev/null
        done
        return
    fi

    echo "$FUNCNAME: package 'xdg-utils' or 'exo' is required." >&2
}

#------------------------------------------------------------

## Aliases for the functions above.
## Uncomment an alias if you want to use it.
##

# alias ef='_open_files_for_editing'     # 'ef' opens given file(s) for editing
# alias pacdiff=eos-pacdiff
################################################################################

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

#export LS_COLORS="di=4;44:*.pbs=0;33:*.txt=0;34:*.vtk=0;36:*.vti=0;36:*.cpp=0;32:*.cmake=0;31:*.stl=0;35:*.py=0;32;47:*.csv=0;37;44:$LS_COLORS"

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

#/--- ALIAS ---/
#	----packages----
alias orphans='sudo pacman -Qtdq'
alias rmorphans='sudo pacman -Rns $(pacman -Qtdq)'
alias ins='sudo pacman -S'
alias rem='sudo pacman -Rcns'
#	----mountable----
alias lusb='sudo fdisk -l'
alias musb='sudo udisksctl mount -b '
alias unmusb='sudo udisksctl unmount -b '
#	----apps configuration----
alias sql='sudo -u postgres psql -w dvdrental'
alias awsdatabase='psql -h database-1.cr8zbyiugave.us-east-2.rds.amazonaws.com -p 5432 -U postgres -W postgres'
alias awsdatabaseEXAMEN='psql -h database-instance-tallerdb.cr8zbyiugave.us-east-2.rds.amazonaws.com -p 5432 -U postgres -W erp_ventas'
alias upddiscord='sudo vim /opt/discord/resources/build_info.json'
alias nqtile='vim $HOME/.config/qtile/config.py'
alias dw='cd $HOME/.suckless/dwm/ && sudo nvim config.h'
#	----system----
alias ls=' ls -ghNo --group-directories-first --time-style=+%b_%d --color=auto' 
alias grep='grep --color=auto'
alias sudo='sudo -Es'
alias bat0='echo Battery Remain: $(cat /sys/class/power_supply/BAT0/capacity)'
alias date='date +"%A %d %b -- %H:%M:%S"'
alias cdh='cd $HOME/'
alias cdt='cd $HOME/TextFiles'
alias cdd='cd $HOME/Downloads/'
alias cdD='cd $HOME/.config/'
alias cdp='cd $HOME/Pictures/'
alias cdw='cd $HOME/Pictures/wallpapers'
alias cdg='cd $HOME/GithubRepo'
alias cdgb='cd $HOME/GithubRepo/bunnydelic && clear && ./source'

# /--Prompt Customization-/
PS1='[\w] '
#PS1='['${bold}'\h'${endcol}' \w] '
#PS1=''${bggreen}'  '${endcol}'  ['${bold}'\h'${endcol}' \w] '

#/---Declarative---/
xset r rate 350 60
export EDITOR="nvim"
export OPENER="xdg-open"

#/---RUN AT START TERMINAL---/
#echo -e "/---/ Remember to edit rem-ins.txt packages!! :> /---/"
#~/GithubRepo/fetchtool/fetch.py


