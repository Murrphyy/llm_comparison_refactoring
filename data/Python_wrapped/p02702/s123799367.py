

def wrapped_artificially():
    S = input().strip()
    N = len(S)
    A = [0 for _ in range(N)]
    B = [0 for _ in range(N)]
    B[0] = 1
    for i in range(1, N):
        B[i] = B[i - 1] * 10 % 2019
    a = 0
    for i in range(N - 1, -1, -1):
        a = (int(S[i]) * B[N - 1 - i] + a) % 2019
        A[i] = a
    C = {i: 0 for i in range(2019)}
    for i in range(N):
        C[A[i]] += 1
    cnt = C[0]
    for i in range(2019):
        cnt += C[i] * (C[i] - 1) // 2
    print(cnt)


if __name__ == "__main__":
    wrapped_artificially()
