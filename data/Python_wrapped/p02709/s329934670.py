from sys import stdin, stdout
import math
import bisect
import datetime

def wrapped_artificially():
    n = int(stdin.readline().strip())
    arr = list(map(int, stdin.readline().strip().split()))
    arr.insert(0, 0)
    d = {}
    for i in range(len(arr)):
        d[i] = arr[i]
    arr = sorted(d.items(), key=lambda a: a[1])
    dp = [[0 for i in range(2005)] for j in range(2005)]
    for i in range(1, n + 1):
        dp[i][i] = arr[1][1] * abs(arr[1][0] - i)
    for l in range(2, n + 1):
        pos, val = arr[l]
        for left in range(1, n - l + 2):
            right = left + l - 1
            dp[left][right] = max(dp[left + 1][right] + val * abs(pos - left), dp[left][right - 1] + val * abs(pos - right))
    stdout.writelines(str(dp[1][n]) + '\n')


if __name__ == "__main__":
    wrapped_artificially()
