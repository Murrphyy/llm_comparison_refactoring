

def wrapped_artificially():
    n = int(input())
    a = list(map(int, input().split()))
    plus = dict()
    minus = dict()
    for i in range(n):
        num = i + 1
        p = a[i] + num
        m = num - a[i]
        if p in plus:
            plus[p] += 1
        else:
            plus[p] = 1
        if m in minus:
            minus[m] += 1
        else:
            minus[m] = 1
    c = 0
    for v in plus.keys():
        if v in minus:
            c += plus[v] * minus[v]
    print(c)


if __name__ == "__main__":
    wrapped_artificially()
