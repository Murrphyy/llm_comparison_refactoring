

def wrapped_artificially():
    n, m = map(int, input().split())
    a = map(int, input().split())
    res = n - sum(a)
    if res < 0:
        print(-1)
    else:
        print(res)


if __name__ == "__main__":
    wrapped_artificially()
