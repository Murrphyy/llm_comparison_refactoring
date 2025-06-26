

def wrapped_artificially():
    n = int(input())
    a = [(int(x), int(y)) for x, y in zip(input().split(), range(n))]
    a.sort(reverse=True)
    dp = [[0] * (n + 1) for i in range(n + 1)]
    for i in range(n + 1):
        for j in range(n + 1 - i):
            if i == 0 and j == 0:
                continue
            if i == 0:
                dp[i][j] = dp[i][j - 1] + a[i + j - 1][0] * abs(a[i + j - 1][1] - j + 1)
                continue
            if j == 0:
                dp[i][j] = dp[i - 1][j] + a[i + j - 1][0] * (n - i - a[i + j - 1][1])
                continue
            dp[i][j] = max([dp[i][j - 1] + a[i + j - 1][0] * abs(a[i + j - 1][1] - j + 1), dp[i - 1][j] + a[i + j - 1][0] * (n - i - a[i + j - 1][1])])
    ans = 0
    for i in range(n + 1):
        key = dp[n - i][i]
        if ans < key:
            ans = key
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
