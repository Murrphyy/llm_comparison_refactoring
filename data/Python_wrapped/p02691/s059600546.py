

def wrapped_artificially():
    N = int(input())
    A = list(map(int, input().split()))
    np, nm = ([], [])
    for i in range(N):
        np.append(A[i] + i)
        nm.append(i - A[i])
    sp, sm = (sorted(np), sorted(nm))
    ans = 0
    for i in range(N):
        p, m = (np[i], nm[i])
        l, r = (-1, N)
        while not l + 1 == r:
            x = (l + r) // 2
            if sm[x] <= p:
                l = x
            else:
                r = x
        tmp = l
        l, r = (-1, N)
        while not l + 1 == r:
            x = (l + r) // 2
            if sm[x] < p:
                l = x
            else:
                r = x
        ans += tmp - l
        l, r = (-1, N)
        while not l + 1 == r:
            x = (l + r) // 2
            if sp[x] <= m:
                l = x
            else:
                r = x
        tmp = l
        l, r = (-1, N)
        while not l + 1 == r:
            x = (l + r) // 2
            if sp[x] < m:
                l = x
            else:
                r = x
        ans += tmp - l
    print(ans // 2)


if __name__ == "__main__":
    wrapped_artificially()
