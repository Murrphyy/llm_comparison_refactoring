import itertools
def add(l, N):
    if len(l) == 0:
        b = 1
    else:
        b = l[-1]
    ans = []
    for i in range(b, N + 1):
        ans.append(l + [i])
    return ans

def wrapped_artificially():
    N, M, Q = [int(x) for x in input().split(' ')]
    conditions = [[int(x) for x in input().split(' ')] for _ in range(Q)]
    L = [[]]
    for _ in range(N):
        nex = []
        for l in L:
            nex.extend(add(l, M))
        L = nex
    smax = 0
    for l in L:
        s = 0
        for c in conditions:
            if l[c[1] - 1] - l[c[0] - 1] == c[2]:
                s += c[3]
        if s > smax:
            smax = s
    print(smax)


if __name__ == "__main__":
    wrapped_artificially()
