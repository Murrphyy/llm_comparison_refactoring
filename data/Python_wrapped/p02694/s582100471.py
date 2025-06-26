import sys
from math import sqrt, gcd, ceil, log
from bisect import bisect
from collections import defaultdict, Counter
def solve():
    n = int(input())
    x = 100
    y = 0
    while x < n:
        x += x // 100
        y += 1
    print(y)

def wrapped_artificially():
    inp = sys.stdin.readline
    read = lambda: list(map(int, inp().strip().split()))
    if __name__ == '__main__':
        solve()


if __name__ == "__main__":
    wrapped_artificially()
