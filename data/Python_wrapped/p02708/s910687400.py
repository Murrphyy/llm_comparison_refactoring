import math
from math import gcd
import sys
import itertools
from collections import Counter, deque
def main():
    n, k = map(int, input().split())
    ans = 0
    mn = mx = 0
    for i in range(n + 1):
        j = n - i
        mn += i
        mx += j
        if i + 1 >= k:
            ans += mx - mn + 1
    print(ans % (10 ** 9 + 7))

def wrapped_artificially():
    INF = float('inf')
    input = sys.stdin.readline
    sys.setrecursionlimit(500 * 500)
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
