

def wrapped_artificially():
    N = int(input())
    A = list(map(int, input().split()))
    A = sorted([(a, i) for i, a in enumerate(A)], reverse=True)
    dp = [0] * (N + 1)
    for i in range(N):
        dp2 = dp[:]
        for l in range(i + 1):
            a, pos = A[i]
            dp2[l + 1] = max(dp2[l + 1], dp[l] + abs(pos - l) * a)
            r = i - l + 1
            dp2[l] = max(dp2[l], dp[l] + abs(N - r - pos) * a)
        dp = dp2
    print(max(dp))


if __name__ == "__main__":
    wrapped_artificially()
