

def wrapped_artificially():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    d = [[-1] * n for _ in range(70)]
    for i in range(n):
        d[0][i] = a[i] - 1
    for i in range(1, 70):
        for j in range(n):
            d[i][j] = d[i - 1][d[i - 1][j]]
    dst = 0
    while k:
        i = 70
        while pow(2, i) & k <= 0:
            i -= 1
        dst = d[i][dst]
        k -= pow(2, i)
    print(dst + 1)


if __name__ == "__main__":
    wrapped_artificially()
