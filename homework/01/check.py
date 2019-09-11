#!/usr/bin/env python

import sys
import tarfile

def main():

    path = sys.argv[1]
    tar = tarfile.open(path)

    entries = [i.name for i in tar]
    dirname = entries.pop(0)
    if dirname.startswith('.'):
        dirname = entries.pop(0)
    entries = [e.replace(dirname + '/', '') for e in entries]

    check('images', entries)
    check('images/egyptian-vulture.jpg', entries)
    check('images/pied-kingfisher.jpg', entries)
    check('images/bank-myna.jpg', entries)

    check('documents', entries)
    check('documents/egyptian-vulture.txt', entries)
    check('documents/pied-kingfisher.txt', entries)
    check('documents/bank-myna.txt', entries)

    check('images/allahabad-sangam.jpg', entries, exists=False)

def check(path, list, exists=True):
    result = (path in list) == exists
    if not result:
        if exists:
            print("Uhoh {} doesn't exist".format(path))
        else:
            print("Uhoh {} exists".format(path))
    return result

if __name__ == "__main__":
    main()
