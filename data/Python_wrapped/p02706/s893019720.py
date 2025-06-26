

def wrapped_artificially():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    sa = sum(a)
    if sa <= n:
        print(n - sa)
    else:
        print(-1)


if __name__ == "__main__":
    wrapped_artificially()
