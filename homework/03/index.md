---
title: "Homework 1: The File-System and Command Line"
css: ../../css/page.css
---

Follow these instructions while substituting anywhere you see `{umd-id}` with your UMD Directory ID.

## Setup

1. Download *hw1-files.tar.gz* from the *Homeworks* files in ELMS to your *Projects/inst126* directory.
1. Open Visual Studio Code.
1. Open your folder *Projects/inst126* in Visual Studio Code.
1. Open a bash terminal window using Terminal menu (make sure it's bash!).
1. Unpack the archive file *hw1.tar.gz*: `tar xvfz hw1-files.tar.gz`
1. Rename `hw1-files` directory to your University Directory ID: for example, `mv hw1-files {umd-id}`
1. Change directory: `cd {umd-id}`

## Organize

1. List the contents of the directory: `ls`
1. List the contents of the directory with file sizes: `ls -l`
1. Remove the the largest file: `rm <filename>`
1. Make a directory called *images*: `mkdir images`
1. Make a directory called *documents*: `mkdir documents`
1. Move all of the `.jpg` files to the *images* directory: `mv *.jpg images`
1. Move all of the `.txt` files to the *documents* directory: `mv *.txt documents`

## Package and Upload

1. Change directories up: `cd ..`
1. Package up the your directory as tar file: `tar cvfz {umd-id}.tar.gz {umd-id}`
1. Submit the file to the assignment.

## Rubric:

* Able to unpack tar file (1pt)
* Able to navigate directories (1pt)
* Able to remove a file (1pt)
* Able to move files (1pt)
* Able to package up directory as a tar file (1pt)