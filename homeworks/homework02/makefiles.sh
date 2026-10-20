#!/bin/bash

# Run from inside homework02/question02/
while read -r num; do
  num=${num//$'\r'/}   # strip Windows line endings
  [ -z "$num" ] && continue
  echo "$num" > "file${num}.txt"
done < ../list.txt