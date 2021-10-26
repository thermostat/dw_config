###############################################
# Custom bash changes
# To add, source at the end of your .bashrc
# source ${DW_CONFIG}/custom_bash.sh
###############################################


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


###########################################################################
# Defines - should one day auto-generate/update
###########################################################################
EDITOR='emacs -nw'
PAGER=less

source ${DW_CONFIG}/colors_bash.sh

###########################################################################
# Prompt
###########################################################################
SHORT_PROMPT="\[${txtcyn}\][\$?]\[${txtgrn}\]:\u@\h:\[${txtcyn}\]\W\[${txtgrn}\]\$\[${txtclr}\] "
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


function preview_url()
{
    curl -s -D - $1 | grep -i location: | sed -e 's/location: //Ig';
}


function tmout {
    tmux split-window -b -p 80 "$* | less";
}

###########################################################################

alias lp=long_prompt
alias sp=short_prompt

source ${DW_CONFIG}/bash_aliases
