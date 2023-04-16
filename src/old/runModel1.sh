#!/bin/bash

# folder_path="../data/"

# for file in "$folder_path"*; do
#   if [ -f "$file" ] && [ "${file##*.}" = "json" ]; then
#     read -p "Do you want to run the Python script on $file? (y/n) " answer
#     if [ "$answer" = "y" ]; then
#       gtimeout 5s python3 model1.py -data="$file" -solve
#     fi
#   fi
# done

folder_path="../data"
time_file="../time/time.txt"

# Create the time file if it doesn't exist
touch "$time_file"

files=("$folder_path"/*.json)

for file in "${files[@]}"; do
  echo "Running the Python script on file: $file"
  start_time=$(date +%s.%N)
  gtimeout 30s python3 model1.py -data="$file" -solve > "${file}.txt" 2>&1
  end_time=$(date +%s.%N)
  elapsed_time=$(echo "$end_time - $start_time" | bc)
  echo "Execution time for $file: $elapsed_time seconds"
  echo "$file: $elapsed_time seconds" >> "$time_file"
done
