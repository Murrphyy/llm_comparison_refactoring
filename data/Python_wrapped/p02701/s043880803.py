import math
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
    N = I()
    S = [_S() for _ in range(N)]
    ans = 0
    s = set()
    for i in range(N):
        s.add(S[i])
    ans = len(s)
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
