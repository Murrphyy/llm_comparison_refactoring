

def wrapped_artificially():
    N = int(input())
    A = list(map(int, input().split()))
    B = []
    for i in range(N):
        B.append([A[i], i + 1])
    B.sort(reverse=True)
    DP = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    for i in range(N):
        I = i + 1
        b, ind = B[i]
        for j in range(I + 1):
            if j == 0:
                DP[j][I - j] = DP[j][I - j - 1] + b * abs(N - (I - j) - ind + 1)
            elif I - j == 0:
                DP[j][I - j] = DP[j - 1][I - j] + b * abs(ind - j)
            else:
                DP[j][I - j] = max(DP[j][I - j - 1] + b * abs(N - (I - j) - ind + 1), DP[j - 1][I - j] + b * abs(ind - j))
    ans = 0
    for i in range(N + 1):
        ans = max(ans, DP[i][N - i])
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
