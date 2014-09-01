# Configuration file for ipython.

c = get_config()

c.TerminalInteractiveShell.color_info = True
c.TerminalInteractiveShell.banner1 = "IPython ..." 
c.TerminalInteractiveShell.banner2 = '... Ready'

c.TerminalInteractiveShell.confirm_exit = False
c.InteractiveShellApp.exec_files = []
c.TerminalInteractiveShell.editor = 'emacs'
