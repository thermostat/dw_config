#!/usr/bin/env python

################################################
# The plan is to migrate from notes to 
# automation
################################################

# Starting package install
# Python-based
# sudo apt-get install ipython ipython-notbook mercurial python-pygments python-docutils
# 
# Others
# sudo apt-get install tmux texlive fluxbox emacs ssh 

# git config --global user.name "$NAME"
# git config --global user.email "$EMAIL"

import os, os.path

config_loc = {
    'tmux': ['{env[HOME]}/.tmux.conf'] 
    'bash': ['{env[HOME]}/.bashrc']
    'emacs' : ['{env[HOME]}/.emacs.d/init.el']
}

config_include_lines {
    'emacs': '(load-file "{dw_config_home}/dww-custom.el")'
}


def find_config_loc(tool):
    cl = config_loc[tool]
    for f in cl:
        resolved = f.format(env=os.environ)
        if os.path.exists(resolved):
            return resolved
    # If none exist, give the first
    return cl[0].format(env=os.environ)


def append_config(program, appendline):
    cfg_fname = find_config_loc(program)
    fd = file(cfg_fname, 'a')
    fd.seek(0, 2)
    fd.write('\n'+appendline+'\n')
    fd.close()

