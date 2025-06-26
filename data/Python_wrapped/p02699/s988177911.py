import sys
from pprint import pprint as pp
from pprint import pformat as pf
import math
import bisect

def wrapped_artificially():
    sys.setrecursionlimit(10 ** 7)
    if __name__ == '__main__':
        s, w = list(map(int, input().split()))
        if w >= s:
            print('unsafe')
        else:
            print('safe')


if __name__ == "__main__":
    wrapped_artificially()
