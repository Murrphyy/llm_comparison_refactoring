import sys
from math import sqrt, gcd, ceil, log
from bisect import bisect
from collections import defaultdict, Counter
def fix(arr, d=0):
    lis = [0] * len(arr)
    if d:
        gcd_ = arr[-1]
        for i in range(len(arr) - 1, -1, -1):
            gcd_ = gcd(gcd_, arr[i])
            lis[i] = gcd_
    else:
        gcd_ = arr[0]
        for i in range(len(arr)):
            gcd_ = gcd(gcd_, arr[i])
            lis[i] = gcd_
    return lis
def solve():
    k = int(input())
    a, b = read()
    if a % k == 0 or b % k == 0 or a <= b // k * k <= b:
        print('OK')
    else:
        print('NG')

def wrapped_artificially():
    inp = sys.stdin.readline
    read = lambda: list(map(int, inp().strip().split()))
    if __name__ == '__main__':
        solve()


if __name__ == "__main__":
    wrapped_artificially()
