def dfs(l):
    global ans
    if len(l) == n + 1:
        tmp = 0
        for i in range(q):
            if l[B[i]] - l[A[i]] == C[i]:
                tmp += D[i]
        ans = max(ans, tmp)
        return
    x = l[len(l) - 1]
    while x <= m:
        y = l[:]
        y.append(x)
        dfs(y)
        x += 1

def wrapped_artificially():
    n, m, q = map(int, input().split())
    A = []
    B = []
    C = []
    D = []
    for i in range(q):
        a, b, c, d = map(int, input().split())
        A.append(a)
        B.append(b)
        C.append(c)
        D.append(d)
    ans = 0
    dfs([1])
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
