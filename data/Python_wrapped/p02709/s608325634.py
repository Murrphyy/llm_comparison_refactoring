

def wrapped_artificially():
    N = int(input())
    A = enumerate(map(int, input().split()))
    A = sorted(A, reverse=True, key=lambda x: x[1])
    DP = [[0] * (N + 1) for x in range(N + 1)]
    for i in range(1, N + 1):
        b, a = A[i - 1]
        b += 1
        for j in range(i + 1):
            c = 0
            if i >= 1 and j >= 1:
                dst = j
                c = max(c, DP[i - 1][j - 1] + a * abs(b - dst))
            if i != j:
                dst = N - (i - j) + 1
                c = max(c, DP[i - 1][j] + a * abs(b - dst))
            DP[i][j] = c
    print(max(DP[N]))


if __name__ == "__main__":
    wrapped_artificially()
