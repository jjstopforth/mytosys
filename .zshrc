# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000
setopt autocd extendedglob nomatch
unsetopt beep
bindkey -v
# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle :compinstall filename '/home/julius/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall

autoload -Uz promptinit
promptinit

autoload -U colors
colors

PROMPT="%{$fg_bold[cyan]%}%n@%m%{$reset_color%}:%{$fg[yellow]%}%1~%{$reset_color%}φ "
alias ls="ls -l --color=auto"

export CONFIG=~/mitosys
