

def wrapped_artificially():
    n, m = map(int, input().split())
    a = map(int, input().split())
    s = 0
    for i in a:
        s += i
    if n - s >= 0:
        print(n - s)
    else:
        print(-1)


if __name__ == "__main__":
    wrapped_artificially()
