#!/usr/bin/env python2
#!/usr/bin/env python

"""
# Alias generation #

Invoked by:

    python scripts/create_aliases.py

"""


import os, os.path
from os.path import join

def find_aliases():
    if os.path.exists('./aliases'):
        return './aliases'
    if os.path.exists('../aliases'):
        return '../aliases'
    p = join(os.environ['HOME'], 'dw_config/aliases')
    if os.path.exists(p):
        return p
    if 'DW_CONFIG' in os.environ:
        p = join(os.environ['DW_CONFIG'], 'aliases')
        return p

def gen_bash_alias(alias_fname, bash_fname):
    fd = open(alias_fname, 'r')
    outfd = open(bash_fname, 'w')
    for line in fd:
        if line.strip().startswith('#'):
            outfd.write(line+"\n")
        else:
            line_data = line.split('=', 1)
            if len(line_data) > 1:
                key = line_data[0].strip()
                val = line_data[1].strip()
                outfd.write("alias {}='{}'\n".format(key,val))
    fd.close()
    outfd.close()
    


if __name__ == '__main__':
    src_alias = find_aliases()
    tgt_alias = join(os.environ['HOME'], '.bash_aliases')
    gen_bash_alias(src_alias, tgt_alias)
