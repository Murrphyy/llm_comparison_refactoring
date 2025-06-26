def func(a):
    if a[-1] != m:
        a[-1] += 1
        return a
    else:
        d = n - 1
        while d > 0 and a[d] == m:
            d = d - 1
        if d < 0:
            return a
        else:
            a[d] += 1
            for x in range(d, n):
                a[x] = a[d]
            return a

def wrapped_artificially():
    n, m, q = map(int, input().split())
    abcd = [list(map(int, input().split())) for _ in range(q)]
    a = [1] * n
    ans = 0
    a[-1] = 0
    while sum(a) != n * m:
        func(a)
        di = 0
        for i in range(q):
            if a[abcd[i][1] - 1] - a[abcd[i][0] - 1] == abcd[i][2]:
                di += abcd[i][3]
        ans = max(ans, di)
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
