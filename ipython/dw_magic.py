
import IPython, json, os.path

ip = IPython.get_ipython()

def jsonsave(self, line):
    obj = self.shell.user_ns[line.strip()]
    basedir = IPython.get_ipython().profile_dir.location
    fname = os.path.join(basedir, 'jsonsave')
    fd = file(fname, 'w')
    json.dump(obj, fd)
    fd.close()

def jsonload(self, line):
    basedir = IPython.get_ipython().profile_dir.location
    fname = os.path.join(basedir, 'jsonsave')
    fd = file(fname, 'r')
    obj = json.load(fd)
    return obj

ip.define_magic('jsonsave', jsonsave)
ip.define_magic('jsonload', jsonload)
del jsonsave
del jsonload
