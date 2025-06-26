from collections import defaultdict as dd
from collections import deque
import bisect
import heapq
def ri():
    return int(input())
def rl():
    return list(map(int, input().split()))
def solve():
    k = ri()
    a, b = rl()
    for i in range(k, 1001, k):
        if a <= i <= b:
            print('OK')
            return
    print('NG')

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
