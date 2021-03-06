# Configuration file for ipython.

"""
ipython profile create danw
echo "execfile('/home/danw/dw_config/ipython/ipython_config.py')" > \
  `ipython locate danw`/profile_pyrento/ipython_config.py
"""

import imp
def add_import(name, result_lst):
    try:
        imp.find_module(name)
        c = get_config()
        c.TerminalIPythonApp.exec_lines.append('import {}'.format(name))
        result_lst.append('  [yes {}]'.format(name))
    except ImportError, e:
        result_lst.append('  [no  {}]'.format(name))
        return False
    return True


# Note, this executes in a different environment from
# the IPython notebook env. You must use the "exec_lines" array
# below to add code that will be executed in the IPython env
c = get_config()

c.TerminalInteractiveShell.color_info = True
c.TerminalInteractiveShell.banner1 = "IPython ..."
c.TerminalInteractiveShell.confirm_exit = False
c.InteractiveShellApp.exec_files = []
c.TerminalInteractiveShell.editor = 'emacs'
c.TerminalIPythonApp.exec_lines = []

banner2 = ['Loading..']
if add_import('pyrento', banner2):
    el = c.TerminalIPythonApp.exec_lines
    el.append('from pyrento.datatype import Address as Addr')
add_import('matplotlib', banner2)
add_import('numpy', banner2)

# Set the end banner
banner2.append("...Ready")
c.TerminalInteractiveShell.banner2 = "\n".join(banner2)
