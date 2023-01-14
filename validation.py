from os import path

def dir_valid(dir):
    valid_dir = path.isdir(dir)

    if not valid_dir:
        raise NotADirectoryError("GitHub directory not a valid directory.")