import sys
import math
import copy
from heapq import heappush, heappop, heapify
from functools import cmp_to_key
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque, Counter
def solve():
    n = getN()
    li = [0 for i in range(n)]
    for nn in getList():
        li[nn - 1] += 1
    for nn in li:
        print(nn)
def main():
    n = getN()
    for _ in range(n):
        solve()
    return

def wrapped_artificially():
    input = sys.stdin.readline
    getS = lambda: input().strip()
    getN = lambda: int(input())
    getList = lambda: list(map(int, input().split()))
    getZList = lambda: [int(x) - 1 for x in input().split()]
    INF = float('inf')
    MOD = 10 ** 9 + 7
    divide = lambda x: pow(x, MOD - 2, MOD)
    if __name__ == '__main__':
        solve()


if __name__ == "__main__":
    wrapped_artificially()
