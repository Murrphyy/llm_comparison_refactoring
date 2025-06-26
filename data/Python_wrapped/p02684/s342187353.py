

def wrapped_artificially():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    v = [-1] * (N + 1)
    n = 1
    for i in range(N):
        v[n] = i
        n = A[n]
        if v[n] != -1:
            s = n
            t = i
            l = t - v[s] + 1
            break
    if t >= K:
        print(v.index(K))
    else:
        K = (K - v[s]) % l
        print(v.index(K + v[s]))


if __name__ == "__main__":
    wrapped_artificially()
