"""
Python 3.6
@Author: wrgsRay
"""
import os

# TODO: Ask user for path
path_base = '.\\test'


def main():
    files = [f for f in os.listdir(path_base) if os.path.isfile(os.path.join(path_base, f))]  # Get all files
    for f in files:
        # TODO: do something
        
        print(f)


if __name__ == '__main__':
    main()
