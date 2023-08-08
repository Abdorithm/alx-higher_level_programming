#!/usr/bin/python3
for i in range(-122, -96):
    print("{}".format(chr((-32-i) if (-i) % 2 != 0 else (-i))), end="")
