# Homework 2: Unix shell

This homework will assess your ability to run commands in the shell and make a simple script.

Replace the lines specified in _italics_ with your answers and save as a text file.


## Problem 0

**60 points**

Complete the interactive tutorial.

_Did you hit any points of frustration, and if so, how could we improve the material to avoid that frustration? If there is something that you would have liked to learn that we left out please let us know so in future years it can be included_


## Problem 1

**20 points**

**Write a script that outputs some user and location data and moves that output to a newly created directory**

Make a single script that prints out a file called question01.txt. 

This file should contain the following text:

  My username is (your username, but the script needs to work for anyone, not just you)

  My home directory is (your home directory, but the script needs to work for anyone, not just you)

  The contents of the tfcb_2023/lectures/lecture04/ directory are

  (prints the contents of that directory)

This script should also create a directory called homework02, and move question01.txt into the homework02 directory.

An example output answer should be:

My username is campbellm <br>
My home directory is /Users/melody <br>
The contents of the tfcb_2023/lectures/lecture04/ directory are<br>
01-first-steps.md<br>
02-directories<br>
03-redirection<br>
04-vim<br>
05-history<br>
06-scripting<br>
07-more-interactive-shell<br>
README.md<br>
quickref.md<br>
sequence.gb<br>
slides<br>
vader.txt<br>

_Paste your SCRIPT here (not the output)_
#!/bin/bash

# Create the output directory (no error if it already exists)
mkdir -p homework02

# Write the user/location info to question01.txt
{
  echo "My username is $(whoami)"
  echo "My home directory is $HOME"
  echo "The contents of the tfcb_2026/lectures/lecture04/ directory are"
  ls "$HOME/tfcb_2026/lectures/lecture04/"
} > question01.txt

# Move the file into homework02
mv question01.txt homework02/


## Problem 2

**20 points**

**Write a script that uses a loop to output files with specific names**


Make a single script that does the following:

Makes a new directory in homework02 called question02

In that directory, your script should make 25 new files called
file###.txt

the ### should be the numbers from a list you can find here:

tfcb_2026/homeworks/homework02/list.txt

You can make the contents of those files whatever you want (hint: slide 9... )

_Paste your SCRIPT here (not the output)_
#!/bin/bash

# Run from the directory that contains homework02/
mkdir -p homework02/question02

(base) root@5828110fe44e:/workspaces/tfcb_2026/homeworks# cd ./homework02
(base) root@5828110fe44e:/workspaces/tfcb_2026/homeworks/homework02# cd ./question02

while read -r num; do
  num=${num//$'\r'/}   # strip Windows line endings
  [ -z "$num" ] && continue
  echo "This is file $num" > "homework02/question02/file${num}.txt"
done < homework02/list.txt


