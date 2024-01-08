
(message "tmux emacs tools el ran")

(setq  tmux_session_name
 (replace-regexp-in-string "\n$" "" 
 (shell-command-to-string "tmux display-message -p -F \"#{session_name}\"")
 ))


(setq tmux_save_dir (format "/home/danw/.config/tmux_sessions/%s" tmux_session_name))



(when (and (getenv "TMUX_PANE")
	 (file-directory-p tmux_save_dir))	 
    (require 'desktop)
    (setq desktop-path (list tmux_save_dir))
    (desktop-save-mode 1)
  )

