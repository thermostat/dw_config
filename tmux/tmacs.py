#!/usr/bin/python

"""
TMacs - open a file in the emacs window 
"""

import tmuxp
import re, os, os.path, sys

EMACS_NAME = re.compile(r'[Ee]macs')

def query_sesh(sesh_list):
    print "Too many sessions: {}".format(sesh_list)
    exit(1)

def find_emacs_window(sesh):
    for w in sesh.windows:
        if EMACS_NAME.search(w['window_name']):
            return w

def raw_send_keys(window, keys):
    window.panes[0].cmd('send-keys', keys)
        
def send_emacs_open(emacs_win, fname):
    fname = os.path.abspath(fname)
    # C-x C-f C-a C-k [fname] Enter
    raw_send_keys(emacs_win, 'C-x')
    raw_send_keys(emacs_win, 'C-f')
    raw_send_keys(emacs_win, 'C-a')
    raw_send_keys(emacs_win, 'C-k')
    raw_send_keys(emacs_win, fname)
    raw_send_keys(emacs_win, 'Enter')
        
def doit(fname):
    s = tmuxp.Server()
    sesh_list = s.attached_sessions()
    sesh = None
    if len(sesh_list) > 1:
        sesh = query_sesh(sesh_list)
    elif len(sesh_list) == 0:
        print "No session"
        exit(1)
    else:
        sesh = sesh_list[0]
    emacs_win = find_emacs_window(sesh)
    send_emacs_open(emacs_win, fname)
    emacs_win.select_window()
    

if __name__ == '__main__':
    doit(sys.argv[1])
