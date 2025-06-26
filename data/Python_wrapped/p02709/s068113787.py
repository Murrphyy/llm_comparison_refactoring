def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 7)
    from collections import Counter, deque
    from itertools import combinations, permutations, accumulate, groupby, product
    from bisect import bisect_left, bisect_right
    from heapq import heapify, heappop, heappush
    import math
    n = int(input())
    a = list(map(int, input().split()))
    l = []
    for i in range(n):
        l.append([a[i], i])
    l.sort(reverse=True)
    dp = [[0] * (n + 1) for _ in range(n)]
    for i in range(n):
        if i == 0:
            dp[i][0] = l[i][0] * (n - 1 - l[i][1])
            dp[i][1] = l[i][0] * l[i][1]
        else:
            for j in range(n, -1, -1):
                if dp[i - 1][j] > 0:
                    dp[i][j + 1] = max(dp[i][j + 1], dp[i - 1][j] + l[i][0] * abs(j - l[i][1]))
                    dp[i][j] = max(dp[i][j], dp[i - 1][j] + l[i][0] * abs(n - i + j - 1 - l[i][1]))
    print(max(dp[-1]))

def wrapped_artificially():
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
