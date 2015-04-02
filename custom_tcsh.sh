###########################################################################
# Custom tcsh
#
# source /path/to/custom_tcsh.sh
###########################################################################

setenv EDITOR 'emacs -nw'

# default file protection
umask 002


if (-e ~/.aliases) then
   source ~/.aliases 
endif


# DW prompt - similar to bash short prompt
set prompt = "%{\033[36m%}[%?]%{\033[32m%}:%n@%m:%{\033[34m%}%c1%{\033[32m%}%%%{\033[0m%} "

### delete words:
bindkey ^W	backward-delete-word
bindkey ^[^d	delete-word
### cursor movement in word::
bindkey ^F forward-char
bindkey ^B backward-char
bindkey ^R i-search-back

