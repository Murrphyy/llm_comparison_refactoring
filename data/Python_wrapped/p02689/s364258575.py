

def wrapped_artificially():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    G = {i + 1 for i in range(N)}
    for _ in range(M):
        a, b = map(int, input().split())
        if H[a - 1] > H[b - 1]:
            G -= {b}
        elif H[b - 1] > H[a - 1]:
            G -= {a}
        else:
            G -= {a, b}
    print(len(G))


if __name__ == "__main__":
    wrapped_artificially()
