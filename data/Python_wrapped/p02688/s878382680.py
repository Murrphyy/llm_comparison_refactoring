import sys
import numpy as np
from math import ceil as C, floor as F, sqrt
from collections import defaultdict as D, Counter as CNT
from functools import reduce as R
def _X():
    return sys.stdin.readline().rstrip().split(' ')
def _S(ss):
    return tuple(ss) if len(ss) > 1 else ss[0]
def S():
    return _S(_X())
def Ss():
    return list(S())
def _I(ss):
    return tuple([int(s) for s in ss]) if isinstance(ss, tuple) else int(ss)
def I():
    return _I(S())
def _Is(ss):
    return list(ss) if isinstance(ss, tuple) else [ss]
def Is():
    return _Is(I())

def wrapped_artificially():
    ALP = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alp = 'abcdefghijklmnopqrstuvwxyz'
    n, k = I()
    ans = [0] * n
    for _ in range(k):
        x = I()
        ys = Is()
        for y in ys:
            ans[y - 1] += 1
    print(len([a for a in ans if a == 0]))


if __name__ == "__main__":
    wrapped_artificially()
