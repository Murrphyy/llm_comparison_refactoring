

def wrapped_artificially():
    n = int(input())
    a = list(map(int, input().split()))
    b = [[a[i], i] for i in range(n)]
    b.sort(reverse=True)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(n - i + 1):
            k = i + j - 1
            if k == -1:
                continue
            if i == 0:
                dp[i][j] = dp[i][j - 1] + abs(b[k][1] - (n - j)) * b[k][0]
            elif j == 0:
                dp[i][j] = dp[i - 1][j] + abs(b[k][1] - (i - 1)) * b[k][0]
            else:
                dp[i][j] = max(dp[i][j - 1] + abs(b[k][1] - (n - j)) * b[k][0], dp[i - 1][j] + abs(b[k][1] - (i - 1)) * b[k][0])
    ans = 0
    for i in range(n + 1):
        ans = max(ans, dp[i][n - i])
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
