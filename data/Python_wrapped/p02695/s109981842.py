import sys
def input():
    return sys.stdin.readline().strip()
def mapint():
    return map(int, input().split())
from itertools import combinations_with_replacement

def wrapped_artificially():
    sys.setrecursionlimit(10 ** 9)
    N, M, Q = mapint()
    abcd = [list(mapint()) for _ in range(Q)]
    lis = range(1, M + 1)
    ans = 0
    for l in combinations_with_replacement(lis, N):
        tmp = 0
        for a, b, c, d in abcd:
            if l[b - 1] - l[a - 1] == c:
                tmp += d
        ans = max(ans, tmp)
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
