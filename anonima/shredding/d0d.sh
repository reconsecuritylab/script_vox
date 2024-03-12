#!/bin/bash

# Usage function
function show_usage {
    echo -e "\e[1;31mError:\e[0m Usage: $0 <files_to_erase>"
    exit 1
}

# Check if files are provided
if [ "$#" -eq 0 ]; then
    show_usage
fi

# Iterate over files specified by the user
for target_files in "$@"; do
    # Skip directories
    if [ -d "$target_files" ]; then
        continue
    fi

    # Ensure the file is created or has write permissions
    touch "$target_files" || { echo "Failed to create or update permissions for $target_files"; exit 1; }

    # Get the file size
    file_size=$(stat -c%s "$target_files")

    # Skip if file size is 0
    if [ "$file_size" -eq 0 ]; then
        echo -e "\e[1;33m [!] Skipping $target_files: File size is 0.\e[0m"
        continue
    fi

    # overwrite 0xff
    echo -e "\e[1;32m [+] Start 0xff overwrite for $target_files\e[0m"
    for i in {1..3}; do
        echo -ne "\xff" | dd of="$target_files" bs=1 count="$file_size" conv=notrunc 2>&1 > /dev/null
    done

    # execution shred cmd
    echo -e "\e[1;32mStart shred command for $target_files\e[0m"
    for i in {1..3}; do
        shred -u -n 2 -z "$target_files" > /dev/null 2>&1
    done

    echo -e "\e[1;32m [+] File $target_files erased with custom pattern and according to DoD 5220.22-M standard.\e[0m"
done

