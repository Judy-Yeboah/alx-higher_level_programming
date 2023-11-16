#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argLen = len(sys.argv)
    if argLen == 2:
        print("{} argument.".format(argLen - 1))
    elif argLen == 1:
        print("{} arguments:".format(argLen - 1))
    else:
        print("{} arguments:".format(argLen - 1))
    for iterator in range(1, argLen):
        print("{}: {}".format(iterator, sys.argv[iterator]))
