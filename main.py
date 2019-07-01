"""
Python 3.6+
@Author: wrgsRay
"""
import os
import shutil
import tkinter as tk
from tkinter import filedialog


def create_delete_folder(folder):
    try:
        os.makedirs(folder)
        print(f'Folder "{folder}" is created')
    except FileExistsError:
        print(f'Folder "{folder}" is already present')


def main():
    root = tk.Tk()
    root.withdraw()
    path_base = filedialog.askdirectory()  # Ask user for folder
    path_target = os.path.join(path_base, 'delete')  # Set target path
    create_delete_folder(path_target)  # create delete folder
    # os.chdir(path_base)  # Change working folder to path
    raw_formats = ['.ARW', '.CR2']  # Include raw formats to scan

    # Get all file names and convert into a list
    files = [f for f in os.listdir(path_base) if os.path.isfile(os.path.join(path_base, f))]

    # Get all raw files into a list
    raws = list()  # create empty list
    for extension in raw_formats:  # Loop through all supported extensions
        raws += ([raw.upper() for raw in files if raw.endswith(extension)])  # If supported raws and found, add to list

    # Get all jpg files into a list without extension
    jpgs = [jpg[0:-4].upper() for jpg in files if jpg.endswith('.JPG')]
    print(raws)
    for raw in raws:  # Loop through all raw filenames
        if raw[0:-4] not in jpgs:  # Check if each raw file can be matched with a JPG
            print(f'{raw} is not found with a JPG. Moving it to \delete')
            shutil.move(os.path.join(path_base, raw), path_target)  # Move the file to "delete" folder


if __name__ == '__main__':
    main()
