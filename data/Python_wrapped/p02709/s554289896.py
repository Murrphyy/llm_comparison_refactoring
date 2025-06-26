

def wrapped_artificially():
    N = int(input())
    A = list(map(int, input().split()))
    babies = [(a, i) for i, a in enumerate(A)]
    babies.sort(reverse=True)
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    ans = 0
    for l in range(N):
        for r in range(N):
            if l + r == N:
                ans = max(ans, dp[l][r])
                break
            active, index = babies[l + r]
            dp[l][r + 1] = max(dp[l][r + 1], dp[l][r] + abs(index - (N - 1 - r)) * active)
            dp[l + 1][r] = max(dp[l + 1][r], dp[l][r] + abs(index - l) * active)
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
