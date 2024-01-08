

alias tmuxsave='python3 $DW_CONFIG/tmux_save.py save --info $(tmuxinfo)'
alias tmuxrestore='python3 $DW_CONFIG/tmux_save.py restore --info $(tmuxinfo)'
alias tmuxecho='tmux display-message -p'

function tmux_history_file {
    TMHISTFILE=$(tmux display-message -p "/home/danw/.config/tmux_sessions/#{session_name}/HISTORY__#{window_index}__TEXT")
    echo "$TMHISTFILE"

}

function tmux_history_load {

    if ! [[ -z "$TMUX_PANE" ]] ; then
	TMHISTFILE=$(tmux display-message -p "/home/danw/.config/tmux_sessions/#{session_name}/HISTORY__#{window_index}__TEXT")
	if [[ -f "$TMHISTFILE" ]] ; then
	    history -r $TMHISTFILE
	fi
    fi

}

function tmux_history_save {
    if ! [[ -z "$TMUX_PANE" ]] ; then
	TMHISTFILE=$(tmux display-message -p "/home/danw/.config/tmux_sessions/#{session_name}/HISTORY__#{window_index}__TEXT")
	TMHISTDIR=$(tmux display-message -p "/home/danw/.config/tmux_sessions/#{session_name}/")
	mkdir -p $TMHISTDIR
	history -w $TMHISTFILE
    fi
}

