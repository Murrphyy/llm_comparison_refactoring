def conb(l, m):
    ls = l.copy()
    if ls[len(ls) - 1] < m:
        ls[len(ls) - 1] += 1
        return ls
    for i in range(len(ls) - 2, -1, -1):
        if ls[i] < m:
            ls[i] += 1
            for j in range(len(ls) - 1, i, -1):
                ls[j] = ls[i]
            return ls
    return None

def wrapped_artificially():
    n, m, q = map(int, input().split())
    ls = [[1] * n]
    i = 0
    while 1:
        x = conb(ls[i], m)
        if x != None:
            ls.append(x)
        else:
            break
        i += 1
    abcd = []
    l = [i for i in range(1, m + 1)]
    ans = 0
    for j in range(q):
        abcd.append(list(map(int, input().split())))
    for v in ls:
        sum = 0
        for j in range(q):
            if v[abcd[j][1] - 1] - v[abcd[j][0] - 1] == abcd[j][2]:
                sum += abcd[j][3]
        ans = max(ans, sum)
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
