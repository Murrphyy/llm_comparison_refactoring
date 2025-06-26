def cmp(it):
    return -it[1]

def wrapped_artificially():
    n = int(input())
    pos = []
    neg = []
    for i in range(n):
        s = input()
        bal = 0
        mn = 0
        for ch in s:
            if ch == '(':
                bal += 1
            if ch == ')':
                bal -= 1
            mn = min(mn, bal)
        if -mn < bal - mn:
            pos.append((-mn, bal - mn))
        else:
            neg.append((-mn, bal - mn))
    pos.sort()
    neg.sort(key=cmp)
    bal = 0
    ok = True
    for m, b in pos:
        if bal - m < 0:
            ok = False
        bal += b - m
    for m, b in neg:
        if bal - m < 0:
            ok = False
        bal += b - m
    if bal != 0:
        ok = False
    if ok:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    wrapped_artificially()
