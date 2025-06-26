

def wrapped_artificially():
    a, b, c, k = map(int, input().split())
    if k <= a:
        print(k)
    else:
        print(a - (k - a - b))


if __name__ == "__main__":
    wrapped_artificially()
