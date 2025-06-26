import heapq

def wrapped_artificially():
    n = int(input())
    bra = []
    ket = []
    c = []
    for _ in range(n):
        s = input()
        mini = 0
        now = 0
        l = len(s)
        for i in range(l):
            if s[i] == '(':
                now += 1
            else:
                now -= 1
                mini = min(mini, now)
        if now >= 0:
            bra.append([-mini, now])
        c.append(now)
        s = s[::-1]
        mini = 0
        now = 0
        for i in range(l):
            if s[i] == ')':
                now += 1
            else:
                now -= 1
                mini = min(mini, now)
        if now >= 0:
            ket.append([-mini, now])
    check = 0
    for x in c:
        check += x
    if check != 0:
        print('No')
        exit()
    bra.sort()
    now = 0
    here = -1
    n = len(bra)
    pool = []
    for i in range(n):
        while here != n - 1:
            if bra[here + 1][0] <= now:
                here += 1
                heapq.heappush(pool, -bra[here][1])
            else:
                break
        if not pool:
            print('No')
            exit()
        else:
            now -= heapq.heappop(pool)
    ket.sort()
    now = 0
    here = -1
    n = len(ket)
    pool = []
    for i in range(n):
        while here != n - 1:
            if ket[here + 1][0] <= now:
                here += 1
                heapq.heappush(pool, -ket[here][1])
            else:
                break
        if not pool:
            print('No')
            exit()
        else:
            now -= heapq.heappop(pool)
    print('Yes')


if __name__ == "__main__":
    wrapped_artificially()
