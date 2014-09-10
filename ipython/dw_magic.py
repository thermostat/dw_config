###########################################################################
#
# Some basic helpful magic lines
#
###########################################################################

import IPython, json, os.path

ip = IPython.get_ipython()

def jsonsave(self, line):
    """
    Save the json-able object in the profile drop-box.
    """
    obj = self.shell.user_ns[line.strip()]
    basedir = IPython.get_ipython().profile_dir.location
    fname = os.path.join(basedir, 'jsonsave')
    fd = file(fname, 'w')
    json.dump(obj, fd)
    fd.close()

def jsonload(self, line):
    """
    Load json from the ipython profile drop-box (as used by 
    %jsonsave).
    """
    basedir = IPython.get_ipython().profile_dir.location
    fname = os.path.join(basedir, 'jsonsave')
    fd = file(fname, 'r')
    obj = json.load(fd)
    return obj

def html_obj(self, line):
    obj = self.shell.user_ns[line.strip()]
    html = IPython.display.HTML(obj.html())
    return html

ip.define_magic('jsonsave', jsonsave)
ip.define_magic('jsonload', jsonload)
ip.define_magic('html_obj', html_obj)

del jsonsave
del jsonload
del html_obj
