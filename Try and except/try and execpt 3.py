#!/usr/bin/env python
"""
Info about our project comes here
"""


__author__ = "Bo Claes"
__email__ = "bo.claes@student.kdg.be"
__status__ = "Development"


def main():
    try:
        print("Hello")
    except:
        print("Something went wrong")
    else:
        print("Nothing went wrong")

if __name__ == '__main__':  # code to execute if called from command-line
    main()
