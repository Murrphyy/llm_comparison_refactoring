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
    A = rl()
    types = dd(int)
    ans = 0
    for i, h in enumerate(A):
        j = i + 1
        ans += types[j - h]
        types[j + h] += 1
    print(ans)

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
