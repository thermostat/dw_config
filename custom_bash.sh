###############################################
# Custom bash changes
# To add, source at the end of your .bashrc
# source /path/to/custom_bash.sh
###############################################

# If we have an alias file, use it
if [ -x $HOME/.bash_aliases ]; then
    source $HOME/.bash_aliases
fi

# Remedial bash: -z means "string is null"
# :+x If DW_CONFIG is defined, replace with "x"
if [ -z ${DW_CONFIG:+x} ]; then
    # Take a few educated guesses
    if [ -d $HOME/dw_config ]; then
      export DW_CONFIG=$HOME/dw_config
    elif [ -d $HOME/code/dw_config ]; then
      export DW_CONFIG=$HOME/code/dw_config
    fi
fi

if [ -d $HOME/code/pyrento ]; then
  export PYRENTO_HOME=$HOME/code/pyrento
  export PYTHONPATH=$PYTHONPATH:$HOME/code
fi

export txtblk='\e[0;30m' # Black - Regular
export txtred='\e[0;31m' # Red
export txtgrn='\e[0;32m' # Green
export txtylw='\e[0;33m' # Yellow
export txtblu='\e[0;34m' # Blue
export txtpur='\e[0;35m' # Purple
export txtcyn='\e[0;36m' # Cyan
export txtwht='\e[0;37m' # White
export bldblk='\e[1;30m' # Black - Bold
export bldred='\e[1;31m' # Red
export bldgrn='\e[1;32m' # Green
export bldylw='\e[1;33m' # Yellow
export bldblu='\e[1;34m' # Blue
export bldpur='\e[1;35m' # Purple
export bldcyn='\e[1;36m' # Cyan
export bldwht='\e[1;37m' # White
export unkblk='\e[4;30m' # Black - Underline
export undred='\e[4;31m' # Red
export undgrn='\e[4;32m' # Green
export undylw='\e[4;33m' # Yellow
export undblu='\e[4;34m' # Blue
export undpur='\e[4;35m' # Purple
export undcyn='\e[4;36m' # Cyan
export undwht='\e[4;37m' # White
export bakblk='\e[40m'   # Black - Background
export bakred='\e[41m'   # Red
export bakgrn='\e[42m'   # Green
export bakylw='\e[43m'   # Yellow
export bakblu='\e[44m'   # Blue
export bakpur='\e[45m'   # Purple
export bakcyn='\e[46m'   # Cyan
export bakwht='\e[47m'   # White
export txtclr='\e[0m'    # Text Reset

###########################################################################
# Defines - should one day auto-generate/update
###########################################################################
EDITOR='emacs -nw'
PAGER=less

#MacOS color prompt
if [[ `uname` == 'Darwin' ]]; then
  export LSCOLORS=gxBxhxDxfxhxhxhxhxcxcx
  export CLICOLOR=1
fi

###########################################################################
# Prompt
###########################################################################
SHORT_PROMPT="\[${txtcyn}\][\$?]\[${txtgrn}\]:\u@\h:\[${txtblu}\]\W\[${txtgrn}\]\$\[${txtclr}\] "
LONG_PROMPT="${txtpur}###########################################################################${txtclr}\nUser=${txtblu}\u${txtclr} Host=${txtblu}\h${txtclr}\nLast Cmd [${txtpur}\t${txtclr}] Exited $? \nIn ${txtcyn}\w${txtclr} History ${txtcyn}\!${txtclr}\n${txtpur}###########################################################################${txtclr}\n$ "
PS1=${SHORT_PROMPT}
#PS1="[\$?]:\u@\h:\W\$ "

function short_prompt
{
    export PS1=${SHORT_PROMPT}
}

function long_prompt
{
    export PS1=${LONG_PROMPT}
}

function termname() {
    echo -ne "\033]0;"$1"\007"
}

function resource
{
    source ~/.bashrc
}

function path
{
    eval `python3 $DW_CONFIG/scripts/path_tool.py $1 $2`
}

###########################################################################

alias lp=long_prompt
alias sp=short_prompt
