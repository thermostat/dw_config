#!/usr/bin/env python

###########################################################################
# The plan is to migrate from notes to 
# automation
###########################################################################

# Starting package install
# Python-based
# sudo apt-get install ipython ipython-notbook mercurial python-pygments 
# sudo apt-get install python-docutils python-matplotlib python-numpy
# 
# Others
# sudo apt-get install tmux texlive emacs emacs-goodies-el
# sudo apt-get install ssh graphviz fluxbox

# git config --global user.name "$NAME"
# git config --global user.email "$EMAIL"


###########################################################################
# Std imports
###########################################################################
import os, os.path
import argparse

append_cfgs = ['tmux', 'bash', 'emacs', 'csh']

config_loc = {
    'tmux': ['{env[HOME]}/.tmux.conf'],
    'bash': ['{env[HOME]}/.bashrc'],
    'emacs' : ['{env[HOME]}/.emacs.d/init.el'],
    'csh' : ['{env[HOME]}/.cshrc'],
    'ipython' : ['{env[HOME]}/.config/ipython/profile_danw/ipython_config.py',
                 '{env[HOME]}/.ipython/profile_danw/ipython_config.py'],
    'ipython_magic' : ['{env[HOME]}/.config/ipython/profile_danw/startup/01dwm.py',
                       '{env[HOME]}/.ipython/profile_danw/startup/01dwm.py'],
}

config_include_lines = {
    'bash': 'source {dw_config_home}/custom_bash.sh\neval `python /home/danw/dw_config/scripts/create_defines.py`',
    'emacs': '(load-file "{dw_config_home}/dww-custom.el")',
    'tmux': 'source-file {dw_config_home}/tmux_custom',
    'ipython': "load_subconfig('/home/danw/dw_config/ipython/ipython_config.py')",
    'ipython_magic':"execfile('{dw_config_home}/ipython/dw_magic.py')",
    'cshrc' : "source {dw_config_home}/custom_tcsh.sh",
}

class Command(object):
    def __init__(self, ns):
        self.ns = ns

    def run(self, command, **args):
        run_vars = vars(self.ns)
        run_vars.update(args)
        if self.ns.verbose or self.ns.pretend:
            print command.format(**run_vars)
        if not self.ns.pretend:
            os.system(command.format(**run_vars))

    def append_to_file(self, filename, appendstr):
        if self.ns.verbose or self.ns.pretend:
            print "{} =>\n  {}".format(filename,appendstr)
        if self.ns.pretend:
            return
        if not os.path.exists(filename):
            ensure_directory(os.path.split(filename)[0])
            mode = 'w'
        else:
            mode = 'a'
        if self.ns.verbose:
            print "Opening {}, mode ({})".format(filename, mode)
        fd = file(filename, mode)
        fd.seek(0, 2)
        fd.write('\n'+appendstr+'\n')
        fd.close()
        

def ensure_directory(dirname):
    print dirname
    last_dir = os.path.split(dirname)[0]
    if len(last_dir) > 1 and not os.path.isdir(last_dir):
        ensure_directory(last_dir)
    if not os.path.isdir(dirname):
        os.mkdir(dirname)

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

def append_config_file(cmd, program):
    cfg_fname = find_config_loc(program)
    appendline = format_dirs(config_include_lines[program])
    cmd.append_to_file(cfg_fname, appendline)

def ipython_setup(cmd):
    cmd.run('ipython profile create danw')
    cmd.run('''echo "execfile('{dw_config_home}/ipython/ipython_config.py')" > `ipython locate danw`/profile_danw/ipython_config.py''',
            dw_config_home=locate_cfg_home() )

def alias_setup(cmd):
    cmd.run('python {dw_config_home}/scripts/create_aliases.py',
            dw_config_home=locate_cfg_home())


def append_configs(cmd, cfg_lst=append_cfgs):
    for pgm in cfg_lst:
        append_config_file(cmd, pgm)

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Configuration scripting')
    parser.add_argument('--all', action='store_true', help='do everything')
    parser.add_argument('--configs', action='store_true', help='do config')
    parser.add_argument('--ipython', action='store_true', help='do ipython setup')
    parser.add_argument('--alias', action='store_true', help='do alias setup')
    parser.add_argument('--verbose', action='store_true', help='print what operations are being performed')
    parser.add_argument('--pretend', action='store_true', help="don't actually modify")
    args = parser.parse_args()
    did_something = False
    cmd = Command(args)
    if args.all or args.configs:
        try:
            did_something = True
            append_configs(cmd)
        except Exception, e:
            print "Config setup failed: {}".format(str(e))
    if args.all or args.ipython:
        try:
            did_something = True
            ipython_setup(cmd)
        except Exception, e:
            print "IPython setup failed: {}".format(str(e))
    if args.all or args.alias:
        try:
            did_something = True
            alias_setup(cmd)
        except Exception, e:
            print "Alias setup failed: {}".format(str(e))
    if not did_something:
        parser.print_help()
