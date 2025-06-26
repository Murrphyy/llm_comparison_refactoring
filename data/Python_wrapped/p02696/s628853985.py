

def wrapped_artificially():
    a, b, n = map(int, input().split())
    x = b - 1 if n >= b else n
    print(a * x // b + a * (x // b))


if __name__ == "__main__":
    wrapped_artificially()
