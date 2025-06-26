import bisect, collections, copy, heapq, itertools, math, string
import sys
def I():
    return int(sys.stdin.readline().rstrip())
def MI():
    return map(int, sys.stdin.readline().rstrip().split())
def LI():
    return list(map(int, sys.stdin.readline().rstrip().split()))
def S():
    return sys.stdin.readline().rstrip()
def LS():
    return list(sys.stdin.readline().rstrip().split())
def num(self):
    return (-2 * pow(self, 3) + 3 * N * pow(self, 2) + (3 * N + 8) * self) // 6

def wrapped_artificially():
    mod = 10 ** 9 + 7
    N, K = MI()
    ans = num(N + 1) - num(K - 1)
    print(ans % mod)


if __name__ == "__main__":
    wrapped_artificially()
