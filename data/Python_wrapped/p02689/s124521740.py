

def wrapped_artificially():
    n, m = list(map(int, input().split()))
    h = list(map(int, input().split()))
    routes = [[] for _ in range(len(h) + 1)]
    for _ in range(m):
        a, b = list(map(int, input().split()))
        routes[a].append(b)
        routes[b].append(a)
    good = 0
    for i in range(1, len(routes)):
        if len(routes[i]) == 0:
            good += 1
            continue
        if h[i - 1] > max([h[j - 1] for j in routes[i]]):
            good += 1
    print(good)


if __name__ == "__main__":
    wrapped_artificially()
