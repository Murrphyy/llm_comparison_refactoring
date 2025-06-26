import math
import numpy as np
import sys
import os
from operator import mul
from operator import itemgetter
def _S():
    return sys.stdin.readline().rstrip()
def I():
    return int(_S())
def LS():
    return list(_S().split())
def LI():
    return list(map(int, LS()))

def wrapped_artificially():
    sys.setrecursionlimit(10 ** 7)
    if os.getenv('LOCAL'):
        inputFile = basename_without_ext = os.path.splitext(os.path.basename(__file__))[0] + '.txt'
        sys.stdin = open(inputFile, 'r')
    INF = float('inf')
    IINF = 10 ** 18
    MOD = 10 ** 9 + 7
    N, M = LI()
    H = LI()
    AB = [LI() for _ in range(M)]
    p = []
    d = {}
    for i in range(N):
        d[i] = H[i]
    g = [set()] * N
    a = [True] * N
    for i in range(M):
        f = AB[i][0] - 1
        t = AB[i][1] - 1
        if d[t] > d[f]:
            a[f] = False
        elif d[f] > d[t]:
            a[t] = False
        else:
            a[f] = False
            a[t] = False
    print(sum(a))


if __name__ == "__main__":
    wrapped_artificially()
