;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Dan's Emacs customizations.
; 
; This should handle general (non-system specific) options, and
; it should be loaded from init.el or .emacs. Tested on emacs 24.
;
; Dan Williams
; dan@osheim.org
; 2013-2014
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


; Not sure if global-font-lock-mode is necessary in
; this day in age, but I keep it as a remind of .emacs
; past.
(global-font-lock-mode 1)
(line-number-mode 1)
(column-number-mode 1)

; emacs23 doesn't seem to do well with themes
(if (> emacs-major-version 23) (load-theme 'tango-dark) 'nil)
; The red comments were overpowering...
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

; Unicode shortcuts Note, most of the math symbols can be gotten from
; the TeX input method (C-\ "TeX" -- see C-h I). The emoji and
; multi-char entries are not included there. Some are duplicated with
; shorter names (i.e., haert vs \heartsuit)
(setq shortcut-alist '(("smilie" . "☺")
                       ("frown" . "☹")
                       ("shrug" . "¯\\_₍ツ)_/¯")
                       ("disapp" . "ಠ_ಠ")
                       ("flip" . "(╯°□°）╯︵ ┻━┻")
                       ("check" . "✓")
                       ("ankh" . "☥")
                       ("inf" . "∞")
                       ("rarrow" . "→")
                       ("larrow" . "←")
                       ("therefore" . "∴")
                       ("soviet" . "☭")
                       ("skull" . "☠")
                       ("radio" . "☢")
                       ("phone" . "☏")
                       ("qnote" . "♩")
                       ("enote" . "♪")
                       ("gear" . "⚙")
                       ("heart" . "♥")
                       ("diamond" . "♦")
                       ("club" . "♣")
                       ("spade" . "♠")
                       ("peace" . "☮")
                       ("degree" . "º")
                       ("keyboard" . "⌨")
                       ("hourglass" . "⌛")
                       ("recycle" . "♻")
                       ("star-of-david" . "✡")
                       ("cross" . "✝")
                       ("coffee" . "☕")
                       ("umbrella" . "☂")
                       ))


(defun insert-shortcut (in)
  "Inserts the unicode shortcut named"
  (interactive (list
                (completing-read "Shortcut: "
                                 (mapcar 'car shortcut-alist)
                )))
  (let ((val (cdr (assoc in shortcut-alist))))
    (insert (if (eq nil val) "" val)))
)


; Some useful keybindings 
(global-set-key (kbd "C-c i") 'insert-shortcut)
(global-set-key (kbd "C-c ;") 'insert-date)
(global-set-key (kbd "C-c r") 'toggle-read-only)
(global-set-key (kbd "C-x /") 'comment-region)

(setq backup-directory-alist '(("." . "~/.emacs.d/save-files")))
