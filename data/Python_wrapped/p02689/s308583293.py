

def wrapped_artificially():
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    r = []
    g = [1] * n
    for i in range(m):
        ps = [int(i) - 1 for i in input().split()]
        x, y = (ps[0], ps[1])
        if h[x] >= h[y]:
            g[y] = 0
        if h[y] >= h[x]:
            g[x] = 0
    print(sum(g))


if __name__ == "__main__":
    wrapped_artificially()
