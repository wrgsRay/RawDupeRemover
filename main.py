"""
Python 3.6+
@Author: wrgsRay
"""
import os
import shutil
import tkinter as tk
import time
from tkinter import filedialog

raw_formats = ['.ARW', '.CR2']  # Include raw formats to scan


def create_folder(folder):
    try:
        os.makedirs(folder)
        print(f'Folder "{folder}" is created')
    except FileExistsError:
        print(f'Folder "{folder}" is already present')


def main():
    root = tk.Tk()
    root.withdraw()
    extra_raw_counter = 0
    extra_jpg_counter = 0
    path_base = filedialog.askdirectory()  # Ask user for folder
    if path_base == '':
        print('It looks like you did not select a folder. The program will end in 5 seconds.')
        time.sleep(5)
        quit()
    extra_raws_path = os.path.join(path_base, 'extra_raws')  # Set path for extra raw files
    extra_jpgs_path = os.path.join(path_base, 'extra_jpgs')  # Set path for extra jpg files
    create_folder(extra_raws_path)  # create delete folder
    create_folder(extra_jpgs_path)  # create delete folder

    # Get all file names and convert into a list
    files = [f for f in os.listdir(path_base) if os.path.isfile(os.path.join(path_base, f))]

    # Get all raw files into a list
    raws = list()  # create empty list
    for extension in raw_formats:  # Loop through all supported extensions
        raws += ([raw.upper() for raw in files if raw.endswith(extension)])  # If supported raws and found, add to list

    # Get all jpg files into a list
    jpgs = [jpg.upper() for jpg in files if jpg.endswith('.JPG') and not jpg.startswith('.')]

    for raw in raws:  # Loop through all raw filenames
        if raw[0:-4] not in [j[0:-4] for j in jpgs]:  # Check if each raw file can be matched with a JPG
            print(f'{raw} is not found with a JPG. Moving it to {extra_raws_path}')
            shutil.move(os.path.join(path_base, raw), extra_raws_path)  # Move the file to "extra_raws_path" folder
            extra_raw_counter += 1
    for jpg in jpgs:
        if jpg[0:-4] not in [r[0:-4] for r in raws]:
            print(f'{jpg}.jpg is not found with a raw file. Moving it to {extra_jpgs_path}')
            shutil.move(os.path.join(path_base, jpg), extra_jpgs_path)  # Move the file to "extra_raws_path" folder
            extra_jpg_counter += 1

    print(f'Operation completed. Found {extra_raw_counter} extra raw files. Found {extra_jpg_counter} extra jpg files.')
    print(f'Program Exiting in 5 seconds')
    time.sleep(5)


if __name__ == '__main__':
    main()
