

def wrapped_artificially():
    N = int(input())
    alist = list(map(int, input().split()))
    a2list = []
    for i in range(N):
        a2list.append((alist[i], i))
    a2list.sort(reverse=True)
    dp = []
    for i in range(N + 1):
        dp.append([0] * (N + 1))
    for i in range(1, N + 1):
        aa, ii = a2list[i - 1]
        for j1 in range(i + 1):
            j2 = i - j1
            if j1 == 0:
                dp[j1][j2] = dp[j1][j2 - 1] + aa * abs(N - 1 - (j2 - 1) - ii)
            elif j2 == 0:
                dp[j1][j2] = dp[j1 - 1][j2] + aa * abs(ii - (j1 - 1))
            else:
                dp[j1][j2] = max(dp[j1][j2 - 1] + aa * abs(N - 1 - (j2 - 1) - ii), dp[j1 - 1][j2] + aa * abs(ii - (j1 - 1)))
    answer = 0
    for i in range(N):
        answer = max(answer, dp[i][N - i])
    print(answer)


if __name__ == "__main__":
    wrapped_artificially()
