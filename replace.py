#!/usr/bin/env python3

from sys import argv

path = argv[1]
oldpattern = argv[2]
newpattern = argv[3]

#traversing directories
def traverse_path(path):
    print(str(path.absolute()))
    if path.is_dir():
        #change the name if it has oldpattern
        for entry in path.iterdir():
            print_path(entry)
    if path.is_file():
        #change name of file if it has oldpattern
        #open file and replace any contents there

traverse_path(path)

if path.contains(oldpattern):
    print(path)
    path.replace(oldpattern, newpattern)
