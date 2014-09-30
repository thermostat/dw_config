# Dan's configuration file for ipython-notebook.

import imp

c = get_config()

def add_import(name, result_lst):
    try:
        imp.find_module(name)
        c = get_config()
        c.IPKernelApp.exec_lines.append('import {}'.format(name))
        result_lst.append('  [yes {}]'.format(name))
    except ImportError, e:
        result_lst.append('  [no  {}]'.format(name))
        return False
    return True


c.IPKernelApp.exec_lines = []
add_import('pyrento', [])

# The IP address the notebook server will listen on.
c.NotebookApp.ip = '0.0.0.0'

# Whether to open in a browser after starting.
c.NotebookApp.open_browser = False

import os
if os.environ.has_key('IPY_NOTES'):
    c.NotebookManager.notebook_dir = os.environ['IPY_NOTES']
else:
    c.NotebookManager.notebook_dir = os.environ['HOME']

