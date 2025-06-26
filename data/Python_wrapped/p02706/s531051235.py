

def wrapped_artificially():
    n, m, *a = map(int, open(0).read().split())
    d = n - sum(a)
    if d < 0:
        print(-1)
    else:
        print(d)


if __name__ == "__main__":
    wrapped_artificially()
