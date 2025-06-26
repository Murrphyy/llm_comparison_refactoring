

def wrapped_artificially():
    n, m = (int(i) for i in input().split())
    h = [int(i) for i in input().split()]
    g = [[] for i in range(n)]
    for i in range(m):
        a, b = (int(i) for i in input().split())
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)
    cnt = 0
    for i in range(n):
        mx = -1
        for j in g[i]:
            mx = max(mx, h[j])
        cnt += h[i] > mx
    print(cnt)


if __name__ == "__main__":
    wrapped_artificially()
