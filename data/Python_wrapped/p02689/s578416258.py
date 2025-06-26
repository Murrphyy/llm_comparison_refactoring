

def wrapped_artificially():
    n, m = map(int, input().split())
    l = list(map(int, input().split()))
    l = [0] + l
    s = set()
    for i in range(1, n + 1):
        s.add(i)
    d = {}
    for i in range(m):
        a, b = map(int, input().split())
        if a in s:
            s.remove(a)
        if b in s:
            s.remove(b)
        if a in d:
            c = d[a]
            c.append(b)
            d[a] = c
        else:
            d[a] = [b]
        if b in d:
            c = d[b]
            c.append(a)
            d[b] = c
        else:
            d[b] = [a]
    cnt = len(s)
    for o in d:
        p = d[o]
        x = l[o]
        f = 0
        for i in p:
            if x <= l[i]:
                f = 1
                break
        if f == 0:
            cnt = cnt + 1
    print(cnt)


if __name__ == "__main__":
    wrapped_artificially()
