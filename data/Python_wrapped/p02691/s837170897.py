import sys
from collections import Counter

def wrapped_artificially():
    N = int(input())
    A = list(map(int, sys.stdin.readline().rsplit()))
    P = [i + a for i, a in enumerate(A, start=1)]
    Q = [j - a for j, a in enumerate(A, start=1)]
    res = 0
    C = Counter(Q)
    for p in P:
        res += C[p]
    print(res)


if __name__ == "__main__":
    wrapped_artificially()
