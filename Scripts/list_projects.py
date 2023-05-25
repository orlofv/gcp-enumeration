#!/usr/bin/env python3

import os

def main():
    input_str = input("Enter folder ID or path to file containing folder IDs: ")
    if os.path.isfile(input_str):
        print(f"\nReading folder IDs from file: {input_str}\n")
        with open(input_str, 'r') as f:
            folders = f.read().splitlines()
    else:
        print(f"\nUsing folder ID: {input_str}\n")
        folders = [input_str]

    for folder in folders:
        print(f"\033[1;35mFolder: {folder}\033[0m")
        projects = os.popen(f"gcloud projects list --filter=\"parent.id='{folder}'\" --format=\"value(projectId, name)\"").read()
        if projects:
            for project in projects.splitlines():
                project_id, display_name = project.split(None, 1)
                print(f"\033[0;32m{project_id}\033[0m: {display_name}")
            print("\n")
        else:
            print("No projects found\n")

    print("\n\n\033[0;32mEnd\033[0m")

if __name__ == '__main__':
    main()
