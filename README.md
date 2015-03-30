
The dw_config project
===========================================================================

Useful configuration settings. The long-term goal is to provide
single-command setup for tools I use, without including any personal
information. The configs included here are free to use, though they
are not necessarily designed with anyone but the author in mind.

Included tools:

* [Emacs][emacs] (Ref [Emacs Wiki][])
* [Tmux][]
* [IPython Notebook][ipynb]
* bash
* aliases
* [Fluxbox][flxbx] menu

Upcoming:

* tcsh

## Usage ##

Automation is on-going, however, currently, the set_configs.py script
will attempt to find and append to the user's bash, tmux and emacs
initiailiztion files:

    python scripts/set_configs.py --all

You can preview changes via the `pretend` option.

    python scripts/set_configs.py --all --pretend

[emacs]: http://www.gnu.org/software/emacs "Emacs"
[Emacs Wiki]: http://www.emacswiki.org "Emacs Wiki"
[Tmux]: http://tmux.sourceforge.net
[ipynb]: http://ipython.org/ipython-doc/stable/notebook/notebook.html
[flxbx]: http://fluxbox.org/
