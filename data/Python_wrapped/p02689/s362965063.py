def resolve():
    N, M = list(map(int, input().split()))
    H = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(M)]
    good = [True for i in range(N)]
    for a, b in AB:
        a, b = (a - 1, b - 1)
        if H[a] < H[b]:
            good[a] = False
        elif H[a] == H[b]:
            good[a] = False
            good[b] = False
        else:
            good[b] = False
    cnt = 0
    for g in good:
        if g:
            cnt += 1
    print(cnt)

def wrapped_artificially():
    if '__main__' == __name__:
        resolve()


if __name__ == "__main__":
    wrapped_artificially()
