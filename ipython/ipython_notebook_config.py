# Dan's configuration file for ipython-notebook.

c = get_config()

# The IP address the notebook server will listen on.
c.NotebookApp.ip = '0.0.0.0'

# Whether to open in a browser after starting.
c.NotebookApp.open_browser = False

import os
if os.environ.has_key('IPY_NOTES'):
    c.NotebookManager.notebook_dir = os.environ['IPY_NOTES']
else:
    c.NotebookManager.notebook_dir = os.environ['HOME']
