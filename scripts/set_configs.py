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
# sudo apt-get install tmux texlive fluxbox emacs ssh emacs-goodies-el

# git config --global user.name "$NAME"
# git config --global user.email "$EMAIL"

import os, os.path

append_cfgs = ['tmux', 'bash', 'emacs']

config_loc = {
    'tmux': ['{env[HOME]}/.tmux.conf'],
    'bash': ['{env[HOME]}/.bashrc'],
    'emacs' : ['{env[HOME]}/.emacs.d/init.el'],
}

config_include_lines = {
    'bash': 'source {dw_config_home}/custom_bash.sh\neval `python /home/danw/dw_config/scripts/create_defines.py`',
    'emacs': '(load-file "{dw_config_home}/dww-custom.el")',
    'tmux': 'source-file {dw_config_home}/tmux_custom',
}

def locate_cfg_home():
    f = str(__file__)
    dw_cfg_home=os.path.abspath(f)
    dw_cfg_home=dw_cfg_home[:dw_cfg_home.rfind('/')]
    dw_cfg_home = os.path.join(dw_cfg_home, '..')
    return os.path.normpath(dw_cfg_home)


def format_dirs(strn):
    return strn.format(env=os.environ, 
                       dw_config_home=locate_cfg_home())

def find_config_loc(tool):
    cl = config_loc[tool]
    for f in cl:
        resolved = f.format(env=os.environ)
        if os.path.exists(resolved):
            return resolved
    # If none exist, give the first
    return cl[0].format(env=os.environ)

def append_config_file(program):
    cfg_fname = find_config_loc(program)
    appendline = format_dirs(config_include_lines[program])
    print "{} =>\n  {}".format(cfg_fname,appendline)
    fd = file(cfg_fname, 'a')
    fd.seek(0, 2)
    fd.write('\n'+appendline+'\n')
    fd.close()



def append_configs(cfg_lst=append_cfgs):
    for pgm in cfg_lst:
        append_config_file(pgm)


if __name__ == '__main__':
    append_configs()
