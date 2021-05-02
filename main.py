#!/usr/bin/env python3
# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os
from pathlib import Path
import shutil


"""
Get the latest folder that is downloaded.
"""
def get_latest_course_download():
    downloads_path = f'{Path.home()}/Downloads'
    all_subdirs = [f'{downloads_path}/{d}' for d in os.listdir(downloads_path) if os.path.isdir(f'{downloads_path}/{d}')]

    return min(all_subdirs, key=os.path.getmtime)

"""
Move all files from one directory to another
"""
def move_files(source_dir, dest=os.getcwd()):
    files = os.listdir(source_dir)
    course_name = get_course_name(source_dir)
    dest_dir = os.path.join(dest, course_name)

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for file in files:
        shutil.move(os.path.join(source_dir, file), os.path.join(dest_dir, file))
        print(os.path.join(source_dir, file), os.path.join(dest_dir, file))

"""
Get the course name from directory path.
"""
def get_course_name(directory_path):
    return os.path.basename(directory_path)

"""
Change directory to the subdirectory.
"""
def change_dir(dest):
    os.chdir(f"./{dest}")

"""
Initialize git directory
"""
def init_git():
    os.system("git init")

"""
Initialize hub
"""
def hub_create():
    os.system("hub create")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    latest_download_dir = get_latest_course_download()
    move_files(latest_download_dir)
    change_dir(get_course_name(latest_download_dir))
    init_git()
    hub_create()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
