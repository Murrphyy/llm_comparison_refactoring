from __future__ import division, print_function
import sys
import os, sys, bisect, copy
from collections import defaultdict, Counter, deque
def input():
    return sys.stdin.readline()
def mapi(arg=0):
    return map(int if arg == 0 else str, input().split())

def wrapped_artificially():
    if sys.version_info[0] < 3:
        from __builtin__ import xrange as range
        from future_builtins import ascii, filter, hex, map, oct, zip
    if os.path.exists('in.txt'):
        sys.stdin = open('in.txt', 'r')
    if os.path.exists('out.txt'):
        sys.stdout = open('out.txt', 'w')
    s, w = mapi()
    if w >= s:
        print('unsafe')
    else:
        print('safe')


if __name__ == "__main__":
    wrapped_artificially()
