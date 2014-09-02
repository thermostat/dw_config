#!/usr/bin/env python

import os
import os.path
from os.path import join

def locate_cfg_home():
    f = str(__file__)
    dw_cfg_home=os.path.abspath(f)
    dw_cfg_home=dw_cfg_home[:dw_cfg_home.rfind('/')]
    dw_cfg_home = os.path.join(dw_cfg_home, '..')
    return os.path.normpath(dw_cfg_home)



def create_defs():
    if os.path.isdir(join(os.environ['HOME'], 'notes')):
        print "export IPY_NOTES={}".format(join(os.environ['HOME'], 'notes'))
    print "export DW_CONFIG={}".format(locate_cfg_home())
    print "export PYTHONPATH=$PYTHONPATH:{}".format(join(locate_cfg_home(), 
                                                         'scripts'))



if __name__ == '__main__':
    create_defs()
