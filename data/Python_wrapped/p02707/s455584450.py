from collections import defaultdict as dd
from collections import deque
import bisect
import heapq
def ri():
    return int(input())
def rl():
    return list(map(int, input().split()))
def solve():
    n = ri()
    L = [0] * (n + 1)
    for i in rl():
        L[i] += 1
    for i in range(1, n + 1):
        print(L[i])

def wrapped_artificially():
    mode = 's'
    if mode == 'T':
        t = ri()
        for i in range(t):
            solve()
    else:
        solve()


if __name__ == "__main__":
    wrapped_artificially()
