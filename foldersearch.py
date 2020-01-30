#!/usr/bin/env python3
import os
import fnmatch

rootpath = 'C:/Users/student/Documents/Data Structures/recursion/Pictures'

IMAGE_GLOBS = {
    '*.jpg',
    '*.png',
    '*.jpeg',
    '*.gif',
}

def is_image(filename):
    for ext in (IMAGE_GLOBS):
        if fnmatch.fnmatch(filename,'*.jpg') or fnmatch.fnmatch(filename,'*.png'):
        #if fnmatch.fnmatch(filename,ext):
            return True
        else:
            return False
    # placeholder here so the file will compile
    #needs work still

def find_images(rootpath, subpath=''):
    '''
    Generator function that returns the images in the given directory
    tree (includes subdirectories). The returned image paths are relative to
    the given path.

    Use os.listdir() to get the files in the current directory (don't use os.walk
    or glob.glob).
    '''

    dir=os.listdir(rootpath+subpath)
    for path in dir:
        full_path = os.path.join(rootpath,subpath,path)
        if os.path.isdir(full_path):
            for entry in find_images(full_path):
                yield entry
        elif os.path.isfile(full_path):
            if is_image(full_path):
                yield full_path
        else:
            print('Unidentified name %s. It could be a symbolic link' % full_path)

    pass  # placeholder here so the file will compile

