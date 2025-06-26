def resolve():
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    ans = {i for i in range(n)}
    for i in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        if h[a] <= h[b]:
            ans.discard(a)
        if h[b] <= h[a]:
            ans.discard(b)
    print(len(ans))
    return

def wrapped_artificially():
    if __name__ == '__main__':
        resolve()


if __name__ == "__main__":
    wrapped_artificially()
