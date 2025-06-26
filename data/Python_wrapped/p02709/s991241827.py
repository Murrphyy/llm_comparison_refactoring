

def wrapped_artificially():
    N = int(input())
    A = list(map(int, input().split()))
    B = [i for i in range(N)]
    C = []
    for i in range(N):
        C.append([A[i], B[i]])
    C = sorted(C, reverse=True)
    dp = [[0] * (N + 1) for i in range(N + 1)]
    dp[0][0] = 0
    for i in range(1, N + 1):
        dp[i][0] = dp[i - 1][0] + C[i - 1][0] * (-C[i - 1][1] + N - i)
        dp[0][i] = dp[0][i - 1] + C[i - 1][0] * (C[i - 1][1] - i + 1)
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i + j <= N:
                c = C[i + j - 1][0]
                d = C[i + j - 1][1]
                dp[i][j] = max(dp[i - 1][j] + c * abs(N - i - d), dp[i][j - 1] + c * abs(j - d - 1))
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    print(dp[N][N])


if __name__ == "__main__":
    wrapped_artificially()
