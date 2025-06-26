from math import gcd
from math import factorial as f
from math import ceil, floor, sqrt
import bisect
import re
import heapq
from copy import deepcopy
import itertools
from sys import exit
def main():
    s, w = mi()
    if w >= s:
        print(yes)
    else:
        print(no)

def wrapped_artificially():
    ii = lambda: int(input())
    mi = lambda: map(int, input().split())
    li = lambda: list(map(int, input().split()))
    yes = 'unsafe'
    no = 'safe'
    main()


if __name__ == "__main__":
    wrapped_artificially()
