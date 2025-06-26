import itertools

def wrapped_artificially():
    N, M, Q = map(int, input().split())
    max = 0
    s = ''
    for i in range(M):
        s += str(i)
    l = list(itertools.combinations_with_replacement(s, N))
    m = [list(map(int, input().split())) for i in range(Q)]
    for x in l:
        count = 0
        for y in m:
            if int(x[y[1] - 1]) - int(x[y[0] - 1]) == y[2]:
                count += y[3]
        if count > max:
            max = count
    print(max)


if __name__ == "__main__":
    wrapped_artificially()
