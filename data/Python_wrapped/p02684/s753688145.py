

def wrapped_artificially():
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    now = 1
    while k:
        k, f = divmod(k, 2)
        if f:
            now = l[now - 1]
        l = [l[l[i] - 1] for i in range(n)]
    print(now)


if __name__ == "__main__":
    wrapped_artificially()
