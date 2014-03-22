#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""
def url_sort_key(url):
  """if there are many parts of name, separated with '-', sort by second part"""
  match = re.search(r'p-(.*)-(.*).', url)
  if match:
    return match.group(2)
  else:
    return url


def read_urls(filename):
    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""
    # +++your code here+++
    f = open(filename, 'rU')
    host = filename.split('_')
    host = 'http://' + host[1]

    text = f.read()
    f.close()
    exp = r'"GET (\S+)'
    urls = re.findall(exp, text)
    puzzle_urls = []
    for url in urls:
    	puzzle_url = host + url
    	if re.search('puzzle', url) and not puzzle_url in puzzle_urls:
    		puzzle_urls.append(puzzle_url)
    puzzle_urls = sorted(puzzle_urls, key=url_sort_key)
    return puzzle_urls

def download_images(img_urls, dest_dir):
    """Given the urls already in the correct order, downloads
    each image into the given directory.
    Gives the images local filenames img0, img1, and so on.
    Creates an index.html in the directory
    with an img tag to show each local image file.
    Creates the directory if necessary.
    """
    # +++your code here+++
    counter = 1
    if not os.path.exists(dest_dir):
   	    os.makedirs(dest_dir)

    htmlfile = file(os.path.join(dest_dir, 'index.html'), 'w')
    htmlfile.write('<html><body>\n')
    
    for img_url in img_urls:
        img_name = "img" + str(counter) + ".jpg"
        urllib.urlretrieve(img_url, dest_dir + "/" + img_name)
        print 'Downloading', img_url, 'as', img_name
        counter += 1
        htmlfile.write('<img src="' + img_name + '" />')

    htmlfile.write('\n</body></html>')
    htmlfile.close()

def main():
    args = sys.argv[1:]

    if not args:
        print 'usage: [--todir dir] logfile '
        sys.exit(1)

    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    img_urls = read_urls(args[0])

    if todir:
        download_images(img_urls, todir)
    else:
        print '\n'.join(img_urls)

if __name__ == '__main__':
    main()
