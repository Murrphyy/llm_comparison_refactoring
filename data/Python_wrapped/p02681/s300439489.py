import bisect
import cmath
import heapq
import itertools
import math
import operator
import os
import random
import re
import string
import sys
from collections import Counter, defaultdict, deque
from copy import deepcopy
from decimal import Decimal
from functools import lru_cache, reduce
from math import gcd
from operator import add, itemgetter, mul, xor
import numpy as np

def wrapped_artificially():
    if os.getenv('LOCAL'):
        sys.stdin = open('_in.txt', 'r')
    sys.setrecursionlimit(10 ** 9)
    INF = float('inf')
    IINF = 10 ** 18
    MOD = 10 ** 9 + 7
    a = sys.stdin.buffer.readline().decode().rstrip()
    b = sys.stdin.buffer.readline().decode().rstrip()[:-1]
    if a == b:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    wrapped_artificially()
