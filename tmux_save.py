
# As 

import json
import os,os.path
import argparse
import subprocess

SESSION_ROOT='/home/danw/.config/tmux_sessions'
SAVE_FILE='/home/danw/.config/tmux_sessions/sessions.json'

class TmuxWindow:
    def __init__(self, infostrn):
        info = infostrn.split(':', 5)
        self.session_name = info[0]
        self.window_index = info[1]
        self.window_name = info[2]
        self.pane_id = info[3]
        self.pane_pid = info[4]

    def dict(self):
        window_info = {}
        window_info["name"] = self.window_name
        window_info["cwd"] = get_proc_cwd(self.pane_pid)
        window_info["exe"] = get_exe_name(self.pane_pid)
        window_info["idx"] = self.window_index
        window_info["session"] = self.session_name
        histfilename = f"HISTFILE__{self.session_name}__{self.window_index}"
        full_histfilename = os.path.join(SESSION_ROOT, histfilename)
        if os.path.exists(full_histfilename):
            window_info["histfile"] = full_histfilename
        return window_info


    

def run_stdout(cmd, verbose=False, raise_error=False):
    if verbose:
        print(cmd)
    procinfo = subprocess.run(cmd, shell=True, capture_output=True)
    if raise_error and (procinfo.returncode != 0):
        raise Error(cmd)
    return procinfo.stdout.decode('ascii')

def get_current_session():
    return run_stdout('tmux display-message -p "#{session_name}"').strip()


def get_window_info(session=None):
    if session == None:
        session = get_current_session()
    fmt_strn = "#{session_name}:#{window_index}:#{window_name}:#{pane_id}:#{pane_pid}"
    output = run_stdout(f'tmux list-panes -s -t {session} -F "{fmt_strn}"')
    return output

def get_proc_cwd(pid):
    return os.readlink(f"/proc/{pid}/cwd")

def get_exe_name(pid):
    return os.path.basename(os.readlink(f"/proc/{pid}/exe"))

def load_sessions(save_file=SAVE_FILE):
    if not os.path.exists(save_file):
        return {}
    fd = open(save_file, 'r')
    return json.load(fd)

def save_sessions(sessions, save_file=SAVE_FILE):
    fd = open(save_file, 'w')
    json.dump(sessions, fd)
    fd.close()



def update_windows(session_dict):
    infos = get_window_info().strip().split('\n')
    windows = []
    for info in infos:
        windows.append(TmuxWindow(info.strip()))
    for window in windows:
        session_dict[window.window_index] = window.dict()
    

def save_session(args):
    sessions = load_sessions()
    current_session = get_current_session()
    session_dict = {}
    update_windows(session_dict)
    sessions[current_session] = session_dict
    save_sessions(sessions)

def restore_session(args):
    sessions = load_sessions()
    current_session = get_current_session()
    for idx,window_data in sessions[current_session].items():
            print(f"tmux new-window -b -t {idx} -n {window_data['name']} -c {window_data['cwd']};", end='')

def recreate_session(args):
    if args.session == None:
        print("need a session name")
        return
    sessions = load_sessions()
    if args.session not in sessions:
        print(f"no session record found for {args.session}")
        return
    command_list = []
    command_list.append(f"tmux new-s -d -s {args.session}")
    for window_idx,window_info in sessions[args.session].items():
        #tmux new-window -b -n first -t test:1
        cmd = f'tmux new-window -d -b -n {window_info["name"]} -t {window_info["session"]}:{window_idx} -e TMUX_TOOLS_ENABLE=1'
        command_list.append(cmd)

    for cmd in command_list:
        if args.pretend:
            print(cmd)
        else:
            run_stdout(cmd)

def genargs():
    parser = argparse.ArgumentParser()
    parser.add_argument("subcmd", choices=["save", "restore", "recreate"])
    parser.add_argument("--session", "-s", default=None)
    parser.add_argument("--pretend", action="store_true")
    return parser.parse_args()
        
def main(args):
    if args.subcmd == 'save':
        save_session(args)
    elif args.subcmd == 'restore':
        restore_session(args)
    elif args.subcmd == 'recreate':
        recreate_session(args)


if __name__ == '__main__':
    main(genargs())
    
        
    
    
