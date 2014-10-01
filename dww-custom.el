;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Dan's Emacs customizations.
; 
; This should handle general (non-system specific) options, and
; it should be loaded from init.el or .emacs. Tested on emacs 24.
;
; dan@osheim.org
; 2013 
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


; Not sure if global-font-lock-mode is necessary in
; this day in age, but I keep it as a remind of .emacs
; past.
(global-font-lock-mode 1)
(line-number-mode 1)
(column-number-mode 1)

; The red comments were overpowering...
(load-theme 'tango-dark)
(set-face-foreground 'font-lock-comment-face "pink")
(set-face-foreground 'font-lock-comment-delimiter-face "pink")

; I think this is the most reasonable C tabstop 
; for my uses.
(setq-default indent-tabs-mode nil)
(setq c-default-style "user"
      c-basic-offset 4)

(set-terminal-coding-system 'utf-8-unix)

; This keeps the ReST mode from freaking out and
; making the headers illegible.
(setq frame-background-mode 'dark)

; Insert date!
(defun insert-date (dummy)
 "Insert current date." 
 (interactive "P")
 (insert (format-time-string "%m-%d-%Y"))
)

; Unicode shortcuts
(setq shortcut-alist '(("smilie" . "☺")
                       ("shrug" . "¯\\_₍ツ)_/¯")
                       ("check" . "✓")
                       ("ankh" . "☥")
                       ("rarrow" . "→")
                       ("therefore" . "∴")
                       ("soviet" . "☭")
                       ("skull" . "☠")
                       ))


(defun insert-shortcut (in)
  "Inserts the shortcut named"
  (interactive (list
                (completing-read "Shortcut: "
                                 (mapcar 'car shortcut-alist)
                )))
  (insert (cdr (assoc in shortcut-alist)))
)


; Some useful keybindings 
(global-set-key (kbd "C-c i") 'insert-shortcut)
(global-set-key (kbd "C-c ;") 'insert-date)
(global-set-key (kbd "C-c r") 'toggle-read-only)
(global-set-key (kbd "C-x /") 'comment-region)

(setq backup-directory-alist '(("." . "~/.emacs.d/save-files")))
