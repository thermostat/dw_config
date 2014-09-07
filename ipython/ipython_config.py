# Configuration file for ipython.

import imp
def add_import(name, result_lst):
    try:
        imp.find_module(name)
        c = get_config()
        c.TerminalIPythonApp.exec_lines.append('import {}'.format(name))
        result_lst.append('  [yes {}]'.format(name))
    except ImportError, e:
        result_lst.append('  [no  {}]'.format(name))


c = get_config()

c.TerminalInteractiveShell.color_info = True
c.TerminalInteractiveShell.banner1 = "IPython ..." 
c.TerminalInteractiveShell.confirm_exit = False
c.InteractiveShellApp.exec_files = []
c.TerminalInteractiveShell.editor = 'emacs'
c.TerminalIPythonApp.exec_lines = []

banner2 = ['Loading..']
add_import('pyrento', banner2)
add_import('matplotlib', banner2)
add_import('numpy', banner2)

# Set the end banner
banner2.append("...Ready")
c.TerminalInteractiveShell.banner2 = "\n".join(banner2)
