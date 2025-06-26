import sys
from collections import defaultdict, deque
import math
from bisect import bisect_left, bisect_right
def divide(k):
    return pow(k, MOD - 2, MOD)
def make_nck(n):
    ret = [1]
    for i in range(1, n + 1):
        ret.append(ret[-1] * (n + 1 - i) * divide(i) % MOD)
    return ret
def make_nigojyo(n):
    ret = [1]
    for i in range(1, n + 1):
        ret.append(ret[-1] * 25 % MOD)
    return ret
def solve():
    n = getN()
    nums = getList()
    agentss = [num - i for i, num in enumerate(nums)]
    agents = [-num - i for i, num in enumerate(nums)]
    agents.sort()
    agentss.sort()
    ans = 0
    for ag in agentss:
        ans += bisect_right(agents, ag) - bisect_left(agents, ag)
    print(ans)
def main():
    n = getN()
    for _ in range(n):
        solve()

def wrapped_artificially():
    input = sys.stdin.readline
    getS = lambda: input().strip()
    getN = lambda: int(input())
    getList = lambda: list(map(int, input().split()))
    getZList = lambda: [int(x) - 1 for x in input().split()]
    INF = 10 ** 20
    MOD = 10 ** 9 + 7
    if __name__ == '__main__':
        solve()


if __name__ == "__main__":
    wrapped_artificially()
