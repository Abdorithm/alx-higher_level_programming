#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = "arguments:"
    if len(sys.argv) == 1:
        arg = "arguments."
    elif len(sys.argv) == 2:
        arg = "argument:"
    print("{} {}".format(len(sys.argv)-1, arg))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
