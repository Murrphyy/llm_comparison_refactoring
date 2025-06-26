

def wrapped_artificially():
    n = int(input())
    A = list(map(int, input().split()))
    A = sorted([(a, i) for i, a in enumerate(A)], reverse=True)
    dp = [[0] * (n + 1) for i in range(n + 1)]
    for i in range(n):
        for j in range(n - i):
            a, k = A[i + j]
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + abs(k - i) * a)
            dp[i][j + 1] = max(dp[i][j + 1], dp[i][j] + abs(n - j - 1 - k) * a)
    ans = 0
    for i in range(n + 1):
        ans = max(ans, max(dp[i]))
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
