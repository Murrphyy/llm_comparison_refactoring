import bisect
import heapq
import itertools
import math
import numpy as np
from collections import Counter, defaultdict, deque
from copy import deepcopy
from decimal import Decimal
from math import gcd
from operator import add, itemgetter, mul, xor
def cmb(n, r, mod):
    bunshi = 1
    bunbo = 1
    for i in range(r):
        bunbo = bunbo * (i + 1) % mod
        bunshi = bunshi * (n - i) % mod
    return bunshi * pow(bunbo, mod - 2, mod) % mod
def I():
    return int(input())
def LI():
    return list(map(int, input().split()))
def MI():
    return map(int, input().split())
def LLI(n):
    return [list(map(int, input().split())) for _ in range(n)]

def wrapped_artificially():
    mod = 10 ** 9 + 7
    a, b, c, k = MI()
    if a + b >= k:
        print(min(k, a))
    else:
        print(a - (k - a - b))


if __name__ == "__main__":
    wrapped_artificially()
