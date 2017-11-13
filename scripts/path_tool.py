#!/usr/bin/python3
#!/usr/local/bin/python3

"""
Path tool - A quick helper for bash.

To use, add the following to your bash startup sequence:

function path { eval `python3 $DW_CONFIG/scripts/path_tool.py $1 $2` ; }

"""

import os, os.path
import pprint

class Path(object):
    def __init__(self, path_str=None):
        if path_str == None:
            path_str = os.environ['PATH']
        self.path_list = self._parse(path_str)

    def _parse(self, path_str):
        return path_str.split(':')
        
    def push(self, directory):
        self.path_list.insert(0, directory)

    def pop(self):
        del self.path_list[0]

    def __str__(self):
        return ":".join(self.path_list)

    def export(self):
        return "export PATH={}".format(str(self))

if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('action', action='store', nargs='?', default='list',
                   help='one of "push", "pop", or "list"')
    p.add_argument('p1', nargs='*', default=[])
    args = p.parse_args()
    if args.action == 'push':
        pathobj = Path()
        pathobj.push(os.path.abspath(args.p1[0]))
        print(pathobj.export())
    if args.action == 'pop':
        pathobj = Path()
        pathobj.pop()
        print(pathobj.export())
    if args.action == 'list':
        # Note, we're meant to be eval'd (for exports), so
        # we printf here.
        print('printf "{}\\\\n"'.format('\\\\n'.join(Path().path_list)))

    
