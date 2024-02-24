# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000
bindkey -e
# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle :compinstall filename '/home/bbasic/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall
PS1='[%~] '

#	----packages----
alias orphans='sudo pacman -Qtdq'
alias rmorphans='sudo pacman -Rns $(pacman -Qtdq)'
alias ins='sudo pacman -Sy'
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
alias cdd='cd $HOME/Downloads/'
alias cdD='cd $HOME/.config/'
alias cds='cd $HOME/.config/scripts/'
alias cdp='cd $HOME/Pictures/'
alias cdw='cd $HOME/Pictures/wallpapers'
alias cdg='cd $HOME/GithubRepo'
alias cdgb='cd $HOME/GithubRepo/bunnydelic && clear && ./source'

xset r rate 350 60
export EDITOR="nvim"
export OPENER="xdg-open"

#bunnydelic
