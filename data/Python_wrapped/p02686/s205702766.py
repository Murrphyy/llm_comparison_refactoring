

def wrapped_artificially():
    N = int(input())
    Up = []
    Down = []
    for _ in range(N):
        S = input()
        L = [0]
        mi = 0
        now = 0
        for __ in range(len(S)):
            if S[__] == '(':
                now += 1
            else:
                now -= 1
                mi = min(mi, now)
        if now > 0:
            Up.append((mi, now))
        else:
            Down.append((mi - now, mi, now))
    Up.sort(reverse=True)
    Down.sort()
    now = 0
    for i, j in Up:
        if now + i < 0:
            print('No')
            exit()
        else:
            now += j
    for _, i, j in Down:
        if now + i < 0:
            print('No')
            exit()
        else:
            now += j
    if now == 0:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    wrapped_artificially()
