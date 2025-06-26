import itertools
import math
import fractions
import functools

def wrapped_artificially():
    s, w = map(int, input().split())
    if w >= s:
        print('unsafe')
    else:
        print('safe')


if __name__ == "__main__":
    wrapped_artificially()
