

def wrapped_artificially():
    n, m = map(int, input().split())
    h = [0] + [int(x) for x in input().split()]
    miti = []
    for i in range(m):
        tmp = [int(x) for x in input().split()]
        miti.append(tmp)
    good = [0] + [True] * n
    for i in miti:
        if h[i[0]] < h[i[1]]:
            good[i[0]] = False
        elif h[i[1]] < h[i[0]]:
            good[i[1]] = False
        else:
            good[i[0]] = False
            good[i[1]] = False
    print(good.count(True))


if __name__ == "__main__":
    wrapped_artificially()
