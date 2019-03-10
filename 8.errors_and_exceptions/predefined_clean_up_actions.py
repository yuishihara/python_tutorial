#!/usr/bin/env python

import os


def create_file(filename):
    with open(filename, 'w') as f:
        f.writelines(['hello', 'world'])


if __name__ == "__main__":
    create_file("myfile.txt")
    # problematic way
    for line in open("myfile.txt"):
        print(line, end="")
    print()

    # recommended way
    with open("myfile.txt") as f:
        for line in f:
            print(line, end="")
    os.remove('myfile.txt')
