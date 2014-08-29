#!/usr/bin/env python

################################################
# The plan is to migrate from notes to 
# automation
################################################

# Starting package install
# sudo apt-get install tmux ipython texlive fluxbox emacs ssh

# git config --global user.name "$NAME"
# git config --global user.email "$EMAIL"

import os, os.path

config_loc = {'tmux': ['{env[HOME]}/.tmux.conf'] }


def find_config_loc(tool):
    cl = config_loc[tool]
    for f in cl:
        resolved = f.format(env=os.environ)
        if os.path.exists(resolved):
            return resolved
    # If none exist, give the first
    return cl[0].format(env=os.environ)
