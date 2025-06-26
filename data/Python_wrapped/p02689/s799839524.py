

def wrapped_artificially():
    f = lambda: map(int, input().split())
    N, M = f()
    *H, = f()
    g = [[] for _ in range(N)]
    for _ in range(M):
        a, b = f()
        g[a - 1].append(b - 1)
        g[b - 1].append(a - 1)
    print(sum((all((H[j] < H[i] for j in g[i])) for i in range(N))))


if __name__ == "__main__":
    wrapped_artificially()
