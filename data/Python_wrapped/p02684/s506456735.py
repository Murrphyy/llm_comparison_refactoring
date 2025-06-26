

def wrapped_artificially():
    N, K = [int(_) for _ in input().split()]
    A = [int(_) - 1 for _ in input().split()]
    X = [-1 for _ in range(N)]
    X[0] = 0
    k = 0
    p = 0
    while k < K:
        p = A[p]
        k += 1
        if X[p] != -1:
            v = (K - k) % (k - X[p]) + X[p]
            print(X.index(v) + 1)
            exit(0)
        X[p] = k
    print(p + 1)


if __name__ == "__main__":
    wrapped_artificially()
