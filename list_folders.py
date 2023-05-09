#!/usr/bin/env python3

import os

def main():
    folder_input = input("Enter folder ID or file path: ")
    print()
    print("Listing Nested Folders")

    if os.path.isfile(folder_input):
        print(f"Reading folder IDs from file: {folder_input}")
        with open(folder_input) as f:
            for folder in f:
                result = os.popen(f"gcloud resource-manager folders list --folder='{folder.strip()}' --format='table(displayName, ID)'").read()
                if result:
                    print(f"\n\n\033[1;35mParent Folder ID: {folder.strip()}\033[0m")
                    print(result)
    else:
        result = os.popen(f"gcloud resource-manager folders list --folder='{folder_input}' --format='table(displayName, ID)'").read()
        if result:
            print(f"\n\n\033[1;35mParent Folder ID: {folder_input}\033[0m")
            print(result)
        else:
            print(f"No results found for folder ID: {folder_input}")

    print("\n\n\033[0;32mEnd\033[0m")

if __name__ == '__main__':
    main()
