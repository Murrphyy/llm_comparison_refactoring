def resolve():
    N, M, Q = list(map(int, input().split()))
    Q = [list(map(int, input().split())) for _ in range(Q)]
    import itertools
    maxpoint = 0
    for seq in itertools.combinations_with_replacement(range(1, M + 1), N):
        point = 0
        for a, b, c, d in Q:
            if seq[b - 1] - seq[a - 1] == c:
                point += d
        maxpoint = max(maxpoint, point)
    print(maxpoint)

def wrapped_artificially():
    if '__main__' == __name__:
        resolve()


if __name__ == "__main__":
    wrapped_artificially()
