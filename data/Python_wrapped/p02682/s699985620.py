

def wrapped_artificially():
    a, b, c, k = map(int, input().split())
    if k <= a:
        print(k)
    elif k <= a + b:
        print(a)
    else:
        x = a + b + c - k
        y = c - x
        ans = a - y
        print(ans)


if __name__ == "__main__":
    wrapped_artificially()
