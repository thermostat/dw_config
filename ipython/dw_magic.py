###########################################################################
#
# Some basic helpful magic lines
#
###########################################################################

import IPython, json, os.path, urllib2

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

def twitter(self, idn):
    url = 'https://api.twitter.com/1/statuses/oembed.json?id={}'.format(idn)
    result = urllib2.urlopen(url)
    html = None
    if result.getcode() == 200:
        data = result.fp.read()
        js = json.loads(data)
        html = IPython.display.HTML(js['html'])
    else:
        html_x = "<b>No twitter message found</b>"
        html = IPython.display.HTML(html_x)
    return html

ip.define_magic('jsonsave', jsonsave)
ip.define_magic('jsonload', jsonload)
ip.define_magic('html_obj', html_obj)
ip.define_magic('twitter', twitter)

del jsonsave
del jsonload
del html_obj
