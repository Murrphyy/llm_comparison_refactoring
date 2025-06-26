def solve(A, nNow, n, m, q, a, b, c, d):
    if nNow == n:
        ret = 0
        for i in range(q):
            if A[b[i] - 1] - A[a[i] - 1] == c[i]:
                ret += d[i]
        return ret
    elif nNow == 0:
        ret = 0
        for i in range(1, m + 1):
            ret = max(ret, solve(A + [i], nNow + 1, n, m, q, a, b, c, d))
        return ret
    else:
        ret = 0
        for i in range(A[nNow - 1], m + 1):
            ret = max(ret, solve(A + [i], nNow + 1, n, m, q, a, b, c, d))
        return ret
def main():
    n, m, q = map(int, input().split())
    a, b, c, d = [[], [], [], []]
    for _ in range(q):
        ai, bi, ci, di = map(int, input().split())
        a.append(ai)
        b.append(bi)
        c.append(ci)
        d.append(di)
    print(solve([], 0, n, m, q, a, b, c, d))
    return

def wrapped_artificially():
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
