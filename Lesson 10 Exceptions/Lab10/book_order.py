"""
Lab 10 by Monika Szucs A00878763
A script containing the main() function
:author: Monika Szucs
:date: November 15, 2021
"""

import sys
import os


def main():
    print(sys.argv)
    print(sys.argv[0])
    print(sys.argv[1])
    print(sys.argv[2])
    print(len(sys.argv))
    num = 0
    while num < len(sys.argv):
        print(sys.argv[num])
        num += 1

    #print(os.getenv())
    print(os.getcwd())
    path = os.getcwd()
    print(os.path.isfile(path))
    print(os.path.exists(path))
    filename = "test.txt"
    print(os.path.isfile(filename))
    print(os.path.exists(filename))
    full_path = os.path.join(path, filename)
    print(full_path)


if __name__ == '__main__':
    main()