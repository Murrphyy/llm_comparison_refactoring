import math
from math import gcd
import sys
import itertools
def main():
    k = int(input())
    a, b = map(int, input().split())
    for i in range(a, b + 1):
        if i % k == 0:
            print('OK')
            exit()
    print('NG')

def wrapped_artificially():
    INF = float('inf')
    input = sys.stdin.readline
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
