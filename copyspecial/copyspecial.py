#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them



def get_special(fdir):
    """Gets special files from directory"""
    files = os.listdir(fdir)
    result = []
    for item in files:
        match = re.search(r'(\w\w)__(\w+)__', item)
        if (match):
            filepath = os.path.abspath(os.path.join(fdir, item))
            result.append(filepath)
    return result


def print_special(special_files):
    """Prints special files"""
    for special in special_files:
        print special


def copy_special(special_files, pathto):
    """Copies special files to pathto directory"""
    if not os.path.exists(pathto):
        os.mkdir(pathto)
    for special in special_files:
        shutil.copy(special, pathto)
        print special, 'copied to ->', pathto


def zip_special(special_files, zipname):
    """compresses special files to zipname zip folder"""
    for special in special_files:
        print special, 'zip to ->', zipname
  
    cmd = 'zip -j ' + zipname + ' ' + ' '.join(special_files)
    print "running cmd: " + cmd
    (status, output) = commands.getstatusoutput(cmd)
    if status:
      sys.stderr.write(output)
      sys.exit(1)


def main():
    # This basic command line argument parsing code is provided.
    # Add code to call your functions below.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]

    if len(args) == 0:
        print "error: must specify one or more dirs"
        sys.exit(1)

    # +++your code here+++
    # Call your functions
    special = []
    for arg in args:
        special = get_special(arg)

    if (todir):
        copy_special(special, todir)
    else:
        if (tozip):
            zip_special(special, tozip)
        else:
            print_special(special) 
    
if __name__ == "__main__":
    main()
