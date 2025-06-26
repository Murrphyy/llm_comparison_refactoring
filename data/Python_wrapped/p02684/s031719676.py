

def wrapped_artificially():
    N, K = map(int, input().split())
    A = [int(x) - 1 for x in input().split()]
    t, i, dist = (0, 0, {0: 0})
    while K > 0:
        K, i, t = (K - 1, i + 1, A[t])
        if t in dist:
            K %= i - dist[t]
        else:
            dist[t] = i
    print(t + 1)


if __name__ == "__main__":
    wrapped_artificially()
