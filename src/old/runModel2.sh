#!/bin/bash

folder_path="../data/"

for file in "$folder_path"*; do
  if [ -f "$file" ] && [ "${file##*.}" = "json" ]; then
    python3 model2.py $1 -data="$file" -solve
  fi
done
