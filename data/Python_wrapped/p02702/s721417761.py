import sys
import math
import os
import itertools
import string
import heapq
import _collections
from collections import Counter
from collections import defaultdict
from collections import deque
from functools import lru_cache
import bisect
import re
import queue
import decimal
class Scanner:

    @staticmethod
    def int():
        return int(sys.stdin.readline().rstrip())

    @staticmethod
    def string():
        return sys.stdin.readline().rstrip()

    @staticmethod
    def map_int():
        return [int(x) for x in Scanner.string().split()]

    @staticmethod
    def string_list(n):
        return [Scanner.string() for i in range(n)]

    @staticmethod
    def int_list_list(n):
        return [Scanner.map_int() for i in range(n)]

    @staticmethod
    def int_cols_list(n):
        return [Scanner.int() for i in range(n)]
def solve():
    S = Scanner.string()
    N = len(S)
    S = S[::-1]
    p = 1
    total = 0
    cnt = [0 for _ in range(MOD)]
    ans = 0
    for i in range(N):
        cnt[total] += 1
        total += int(S[i]) * p
        total %= MOD
        ans += cnt[total]
        p = p * 10 % MOD
    print(ans)
def main():
    solve()

def wrapped_artificially():
    MOD = 2019
    INF = int(1000000000000000.0)
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
