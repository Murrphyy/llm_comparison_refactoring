import heapq
import math
import random
import sys
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque, namedtuple, UserDict
from functools import cmp_to_key, lru_cache, reduce
from itertools import chain, combinations, combinations_with_replacement, permutations, product
import numpy as np

def wrapped_artificially():
    sys.setrecursionlimit(10 ** 6 + 1)
    write = sys.stdout.write
    input = sys.stdin.buffer.readline
    MOD = 10 ** 9 + 7
    if __name__ == '__main__':
        n = int(input())
        arr = sorted(enumerate(map(int, input().split()), 1), key=lambda x: x[1], reverse=True)
        dp = np.zeros(n + 1, dtype=np.int)
        for k, (i, a) in enumerate(arr, 1):
            ndp = dp.copy()
            add_left = np.abs(np.arange(1, k + 1) - i) * a
            ndp[1:k + 1] = np.maximum(ndp[1:k + 1], dp[:k] + add_left)
            add_right = np.abs(np.arange(n - k + 1, n + 1) - i) * a
            ndp[:k] = np.maximum(ndp[:k], dp[:k] + add_right)
            dp = ndp
        print(dp.max())


if __name__ == "__main__":
    wrapped_artificially()
