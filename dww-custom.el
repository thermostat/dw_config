;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Dan's Emacs customizations.
; 
; This should handle general (non-system specific) options, and
; it should be loaded from init.el or .emacs. Tested on emacs 24.
;
; (load-file {{ PYRENTO_HOME }}/dww-custom.el)
;
; Dan Williams
; dww@pyrento.net
; 2013-2025
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;                                         

;Markdown package -
;http://jblevins.org/projects/markdown-mode/markdown-mode.el
;(browse-url-emacs 
; "http://jblevins.org/projects/markdown-mode/markdown-mode.el")

 (ignore-errors
   (let ((md-file "~/.emacs.d/markdown-mode.el"))
     (if (not (file-exists-p md-file))
         (url-copy-file "https://raw.githubusercontent.com/jrblevin/markdown-mode/master/markdown-mode.el" md-file))
  (load-file md-file)
  ))

; Not sure if global-font-lock-mode is necessary in
; this day in age, but I keep it as a remind of .emacs
; past.
(global-font-lock-mode 1)
(line-number-mode 1)
(column-number-mode 1)

; emacs23 doesn't seem to do well with themes
(if (> emacs-major-version 23) (load-theme 'tango-dark) 'nil)
;(load-theme 'obsidian)
; The red comments were overpowering...
(set-face-foreground 'font-lock-comment-face "pink")
(set-face-foreground 'font-lock-comment-delimiter-face "pink")

; Make cuda (.cu) files register as C++
(add-to-list 'auto-mode-alist '("\\.cu\\'" . c++-mode))
 

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

; Ignore "news," and just go to the file-backed scratch buffer
(setq inhibit-startup-screen t)
(if (file-exists-p "~/.scratch")
    (find-file "~/.scratch"))

(require 'package)
(add-to-list 'package-archives '("melpa" . "https://melpa.org/packages/") t)
(package-initialize)
;(require 'magit)
