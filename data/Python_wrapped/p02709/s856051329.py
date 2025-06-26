

def wrapped_artificially():
    n = int(input())
    a = list(map(int, input().split()))
    li = list(enumerate(a))
    li.sort(key=lambda x: x[1])
    li.reverse()
    dp = [[0 for _ in range(n + 1)] for __ in range(n + 1)]
    ans = 0
    for i in range(n + 1):
        for j in range(n + 1):
            cnt = i + j
            if cnt == 0:
                continue
            if cnt > n:
                continue
            if i == 0:
                dp[0][j] = dp[0][j - 1] + li[cnt - 1][1] * (n - j - li[cnt - 1][0])
                continue
            if j == 0:
                dp[i][0] = dp[i - 1][0] + li[cnt - 1][1] * (li[cnt - 1][0] - (i - 1))
                continue
            res1 = dp[i][j - 1] + li[cnt - 1][1] * (n - j - li[cnt - 1][0])
            res2 = dp[i - 1][j] + li[cnt - 1][1] * (li[cnt - 1][0] - (i - 1))
            dp[i][j] = max(res1, res2)
            if cnt == n:
                ans = max(ans, dp[i][j])
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
