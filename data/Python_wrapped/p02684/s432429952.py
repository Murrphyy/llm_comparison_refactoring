

def wrapped_artificially():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * n
    r = [0] * n
    index = 0
    for i in range(1, n + 1):
        if b[a[index] - 1] != 0:
            break
        b[a[index] - 1] = i
        index = a[index] - 1
    for i in range(1, n + 1):
        if r[a[index] - 1] != 0:
            break
        r[a[index] - 1] = i
        index = a[index] - 1
    maxb = max(b)
    maxr = max(r)
    if k <= maxb:
        print(b.index(k) + 1)
    else:
        k = k - maxb
        if k % maxr == 0:
            print(r.index(maxr) + 1)
        else:
            print(r.index(k % maxr) + 1)


if __name__ == "__main__":
    wrapped_artificially()
