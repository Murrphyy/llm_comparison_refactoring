import sys
from collections import deque
import numpy as np
import math
def S():
    return sys.stdin.readline().rstrip()
def SL():
    return map(str, sys.stdin.readline().rstrip().split())
def I():
    return int(sys.stdin.readline().rstrip())
def IL():
    return map(int, sys.stdin.readline().rstrip().split())
def dfs(l, n, m, e):
    if len(l) == n:
        tmp = 0
        for aa, bb, cc, dd in zip(e[0], e[1], e[2], e[3]):
            if l[bb] - l[aa] == cc:
                tmp += dd
        global ans
        ans = max(ans, tmp)
        return
    x = l[-1] if len(l) else 0
    for i in range(x, m):
        dfs(l + [i], n, m, e)
def Main():
    n, m, q = IL()
    a, b, c, d = ([0] * q, [0] * q, [0] * q, [0] * q)
    for i in range(q):
        a[i], b[i], c[i], d[i] = IL()
        a[i] -= 1
        b[i] -= 1
    e = [a, b, c, d]
    dfs([], n, m, e)
    print(ans)
    return

def wrapped_artificially():
    sys.setrecursionlimit(10 ** 6)
    ans = 0
    if __name__ == '__main__':
        Main()


if __name__ == "__main__":
    wrapped_artificially()
