import subprocess
from datetime import datetime


def status_actions(dir):
    output = subprocess.run(["git", "branch", "--show-current"], capture_output = True, text = True, cwd = dir)
    print("active branch:", output.stdout.rstrip())

    output = subprocess.run(["git", "status", "-z"], capture_output = True, text = True, cwd = dir)
    if output.stdout:
        print("local changes:", True)
    else:
        print("local changes:", False)

def log_actions(dir):
    output = subprocess.run(["git", "log", "-1", "--format=%cd", "--date=short"], capture_output = True, text = True, cwd = dir)
    datetime_str = output.stdout.rstrip()
    present_date = datetime.now()
    commit_date = datetime.strptime(datetime_str, '%Y-%m-%d')
    if (present_date - commit_date).days < 7:
        print("recent commit:", True)
    else:
        print("recent commit:", False)

    output = subprocess.run(["git", "log", "-1", "--pretty=format:%an"], capture_output = True, text = True, cwd = dir)
    if output.stdout.rstrip() == "Rufus":
        print("blame Rufus:", True)
    else:
        print("blame Rufus:", False)
    