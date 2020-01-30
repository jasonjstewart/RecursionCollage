#!/usr/bin/env python3
import argparse
import os
from PIL import Image               # pip3 install pillow
from foldersearch import find_images
import math


THUMNAILS_PER_ROW = 4
THUMBNAIL_WIDTH = 200
THUMBNAIL_HEIGHT = 200



########################
###  Main program

def main(args):
    '''
    Creates a collage by recursively finding images in a directory path.
    '''
    # find the images
    imgpaths = []
    for filepath in find_images(os.path.abspath(args.searchpath)):
        imgpaths.append(filepath)
        print(filepath)
    if len(imgpaths) == 0:
        print('No images found')
        return
    print(imgpaths)
    print("HEY")
    # create a new, RGB image
    collage = Image.new("RGB",(THUMNAILS_PER_ROW*THUMBNAIL_WIDTH,(math.ceil(len(imgpaths)/THUMNAILS_PER_ROW)*THUMBNAIL_HEIGHT))) #THIS WILL NEED TO BE CHANGED
    # place the thumbnails
    current_col=0
    current_row=0
    for imgnum, imgpath in enumerate(imgpaths):
        print(f'=> {imgpath}')
        #open the image and convert to RGB
        im = Image.open(imgpath)
        im.convert(mode='RGB')
        # resize to a thumnail
        im.thumbnail((THUMBNAIL_HEIGHT,THUMBNAIL_WIDTH))
        # paste in next position
        current_col=imgnum % THUMNAILS_PER_ROW
        current_row=math.floor(imgnum/THUMNAILS_PER_ROW)
        collage.paste(im, (THUMBNAIL_WIDTH*current_col,THUMBNAIL_HEIGHT*current_row))


        

    # save the image
    collage.show()
    collage.save(args.collage)
    print(f'Writing {args.collage}')


########################
###  Bootstrap

parser = argparse.ArgumentParser(description='Creates a collage by recursively finding images in a directory path')
parser.add_argument('collage', help='file name to write the collage to')
parser.add_argument('searchpath', help='directory path to start searching')
args = parser.parse_args()
main(args)
