#!/bin/bash

file_paths=("seminararbeit.tex" "preambel.tex")
script_path="scripts/build.sh"

while true; do
    for file_path in "${file_paths[@]}"; do
        if [[ $(stat -c %Y "$file_path") -ne $(stat -c %Y "$file_path" 2>/dev/null) ]]; then
            echo "File '$file_path' has been modified. Running script '$script_path'..."
            bash "$script_path" -no-biber
        fi
    done
    sleep 1
done
