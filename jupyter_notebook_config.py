# dw_config jupyter 

import os.path

if os.path.exists('/home/danw/.jupyter_token'):
    c.NotebookApp.token = open('/home/danw/.jupyter_token', 'r').read().strip()
else:
    c.NotebookApp.token = '<generated>'

if os.path.exists('/home/danw/notes'):
    c.NotebookApp.notebook_dir = '/home/danw/notes'
    
    
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.open_browser = False
