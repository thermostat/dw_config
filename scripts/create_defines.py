#!/usr/bin/env python2
#!/usr/bin/env python

import os
import os.path
from os.path import join
from glob import glob

def locate_cfg_home():
    f = str(__file__)
    dw_cfg_home=os.path.abspath(f)
    dw_cfg_home=dw_cfg_home[:dw_cfg_home.rfind('/')]
    dw_cfg_home = os.path.join(dw_cfg_home, '..')
    return os.path.normpath(dw_cfg_home)



def create_defs():
    home_dir = os.environ['HOME']
    if os.path.isdir(join(home_dir, 'notes')):
        print "export IPY_NOTES={}".format(join(home_dir, 'notes'))
    print "export DW_CONFIG={}".format(locate_cfg_home())
    py_paths = []
    pyrento_dir = glob(join(home_dir, '*/pyrento'))
    if len(pyrento_dir):
        py_paths.append(os.path.split(pyrento_dir[0])[0])
    py_paths.append(join(locate_cfg_home(),'scripts'))
    print "export PYTHONPATH=$PYTHONPATH:{}".format(":".join(py_paths))



if __name__ == '__main__':
    create_defs()
