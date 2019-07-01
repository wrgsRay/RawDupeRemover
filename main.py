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
    extra_raws_path = os.path.join(path_base, 'extra_raws')  # Set path for extra raw files
    extra_jpgs_path = os.path.join(path_base, 'extra_jpgs')  # Set path for extra jpg files
    create_delete_folder(extra_raws_path)  # create delete folder
    raw_formats = ['.ARW', '.CR2']  # Include raw formats to scan

    # Get all file names and convert into a list
    files = [f for f in os.listdir(path_base) if os.path.isfile(os.path.join(path_base, f))]

    # Get all raw files into a list
    raws = list()  # create empty list
    for extension in raw_formats:  # Loop through all supported extensions
        raws += ([raw.upper() for raw in files if raw.endswith(extension)])  # If supported raws and found, add to list

    # Get all jpg files into a list
    jpgs = [jpg.upper() for jpg in files if jpg.endswith('.JPG')]
    # print(raws)
    # print(jpgs)
    for raw in raws:  # Loop through all raw filenames
        print(f'Checking {raw[0:-4]}')
        if raw[0:-4] not in [j[0:-4] for j in jpgs]:  # Check if each raw file can be matched with a JPG
            print(f'{raw} is not found with a JPG. Moving it to \delete')
            shutil.move(os.path.join(path_base, raw), extra_raws_path)  # Move the file to "delete" folder
    # TODO: do the same for JPGS


if __name__ == '__main__':
    main()
