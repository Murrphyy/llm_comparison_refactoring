import math
from math import gcd
import sys
import itertools
import string
def main():
    s = input().rstrip()
    t = input().rstrip()
    for i in range(len(s)):
        if s[i] != t[i]:
            print('No')
            exit()
    if len(t) == len(s) + 1:
        print('Yes')
    else:
        print('No')

def wrapped_artificially():
    INF = float('inf')
    input = sys.stdin.readline
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
