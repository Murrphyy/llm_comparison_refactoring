

def wrapped_artificially():
    N, = map(int, input().split())
    As = list(enumerate(map(int, input().split())))
    As.sort(key=lambda x: -x[1])
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    for i, (pos, val) in enumerate(As):
        for j in range(i + 1):
            k = i - j
            dp[j + 1][k] = max(dp[j + 1][k], dp[j][k] + abs(j - pos) * val)
            dp[j][k + 1] = max(dp[j][k + 1], dp[j][k] + abs(N - 1 - k - pos) * val)
    print(max((dp[i][N - i] for i in range(N + 1))))


if __name__ == "__main__":
    wrapped_artificially()
