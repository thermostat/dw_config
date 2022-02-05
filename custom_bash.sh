###############################################
# Custom bash changes
# To add, source at the end of your .bashrc
# source /path/to/custom_bash.sh
###############################################

# Fix python versions
if which python2.7 > /dev/null; then
    export PYTHON2=python2.7
else
    export PYTHON2=python
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

if [ -r $DW_CONFIG/scripts/create_aliases.py ]; then
  python3 $DW_CONFIG/scripts/create_aliases.py
fi

if [ -d $HOME/code/pyrento ]; then
  export PYRENTO_HOME=$HOME/code/pyrento
  export PYTHONPATH=$PYTHONPATH:$HOME/code
fi

# If we have an alias file, use it
if [ -x $HOME/.bash_aliases ]; then
    source $HOME/.bash_aliases
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

LS_COLORS='rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37:sg=30;43:ca=30:tw=30:ow=34:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.Z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.jpg=01;35:*.jpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:';
export LS_COLORS


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
