

def wrapped_artificially():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    hist = [0 for _ in range(N + 1)]
    hist[1] = 1
    cur = A[1]
    while True:
        cur = A[cur]
        if hist[cur] == 0:
            hist[cur] = 1
        else:
            break
    s = cur
    cur = A[s]
    T = 1
    while cur != s:
        cur = A[cur]
        T += 1
    T1 = 0
    cur = 1
    while cur != s:
        cur = A[cur]
        T1 += 1
    if K <= T1:
        cur = 1
        cnt = 0
        while cnt < K:
            cur = A[cur]
            cnt += 1
        print(cur)
    else:
        K = (K - T1) % T
        cur = s
        cnt = 0
        while cnt < K:
            cur = A[cur]
            cnt += 1
        print(cur)


if __name__ == "__main__":
    wrapped_artificially()
