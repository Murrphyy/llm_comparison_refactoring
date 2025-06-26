import sys, bisect, math, itertools, string, queue, copy
import numpy as np
import scipy
from collections import Counter, defaultdict, deque
from itertools import permutations, combinations
from heapq import heappop, heappush
from fractions import gcd
def inp():
    return int(input())
def inpm():
    return map(int, input().split())
def inpl():
    return list(map(int, input().split()))
def inpls():
    return list(input().split())
def inplm(n):
    return list((int(input()) for _ in range(n)))
def inplL(n):
    return [list(input()) for _ in range(n)]
def inplT(n):
    return [tuple(input()) for _ in range(n)]
def inpll(n):
    return [list(map(int, input().split())) for _ in range(n)]
def inplls(n):
    return sorted([list(map(int, input().split())) for _ in range(n)])

def wrapped_artificially():
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 8)
    mod = 10 ** 9 + 7
    n, m, q = inpm()
    ans = 0
    abcd = []
    for _ in range(q):
        a, b, c, d = inpm()
        abcd.append((a, b, c, d))
    for e in itertools.combinations_with_replacement(range(m), n):
        cnt = 0
        for i in range(q):
            [a, b, c, d] = abcd[i]
            if e[b - 1] - e[a - 1] == c:
                cnt += d
        ans = max(ans, cnt)
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
