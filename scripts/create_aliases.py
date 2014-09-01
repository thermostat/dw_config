#!/usr/bin/env python

def gen_bash_alias(alias_fname, bash_fname):
    fd = file(alias_fname, 'r')
    outfd = file(bash_fname, 'w')
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
    gen_bash_alias('../aliases',
                   '../../.bash_aliases')
