#!/usr/bin/env python3

import argparse
import shutil
import os

if __name__ == '__main__':

    # adds the 'files_number' argument to dlmv.py
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "files_number", 
        type=int,
        nargs='?',
        default=1,  
        help="The number of most recent files to move from the Downloads folder to the current directory (default: 1)"
    )
    args = parser.parse_args()


    downloads_path = os.path.expanduser('~/Downloads')
    paths = [f'{downloads_path}/{path}' for path in os.listdir(downloads_path)]
    if len(paths) < args.files_number:
        files_number = len(paths)
    else:
        files_number = int(args.files_number)

      
    if args.files_number > 0 and len(paths) > 0:

        # selects the paths of specified files
        paths.sort(key=lambda path: os.path.getmtime(path), reverse = True)
        selected = paths[:files_number]

        # prints the confirmation and moves the file if positive
        current_dir = os.getcwd()
        confirmation = input(f'Do you want to move:\n* {"\n* ".join(selected)}\nto {os.getcwd()}? [y/n]: ').lower()
        if confirmation == 'y':
            for path in selected:
                shutil.move(path, current_dir)
            print(f'{files_number} file{"s"*(files_number>1)} moved.')


    elif len(paths) == 0:
        print(f'The Downloads folder is empty.')


    else:
        print(f'{files_number} is an invalid number of files to move.')
