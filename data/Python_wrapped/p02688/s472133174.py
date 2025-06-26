import math
import numpy as np
import sys
import os
from operator import mul
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
    N, K = LI()
    s = set()
    for i in range(K):
        _ = I()
        s.update(LI())
    print(N - len(s))


if __name__ == "__main__":
    wrapped_artificially()
