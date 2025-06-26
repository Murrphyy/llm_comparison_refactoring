import itertools
import math

def wrapped_artificially():
    s, w = map(int, input().split())
    if s <= w:
        print('unsafe')
    else:
        print('safe')


if __name__ == "__main__":
    wrapped_artificially()
