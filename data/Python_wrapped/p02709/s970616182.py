

def wrapped_artificially():
    N = int(input())
    A = list(map(int, input().split()))
    infants = []
    for i, a in enumerate(A):
        infants.append((a, i))
    infants.sort(reverse=True)
    dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    for i in range(N):
        for j in range(i + 1):
            dp[j + 1][i - j] = max(dp[j + 1][i - j], dp[j][i - j] + infants[i][0] * abs(infants[i][1] - j))
            dp[i - j][j + 1] = max(dp[i - j][j + 1], dp[i - j][j] + infants[i][0] * abs(infants[i][1] - (N - 1 - j)))
    ans = 0
    for i in range(N + 1):
        ans = max(ans, dp[i][N - i])
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
