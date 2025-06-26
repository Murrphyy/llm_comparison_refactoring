import bisect
import copy
import heapq
import math
import sys
from collections import *
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0] + list(accumulate(lst))

def wrapped_artificially():
    sys.setrecursionlimit(500000)
    mod = pow(10, 9) + 7
    al = [chr(ord('a') + i) for i in range(26)]
    direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    n = int(input())
    a = list(map(int, input().split()))
    dic = {}
    ans = 0
    for i in range(n):
        if i - a[i] in dic:
            ans += dic[i - a[i]]
        if a[i] + i in dic:
            dic[a[i] + i] += 1
        else:
            dic[a[i] + i] = 1
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
