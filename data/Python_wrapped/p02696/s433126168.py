

def wrapped_artificially():
    a, b, n = map(int, input().split())
    if n >= b - 1:
        x = b - 1
    else:
        x = n
    print(a * x // b - a * (x // b))


if __name__ == "__main__":
    wrapped_artificially()
