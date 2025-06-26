

def wrapped_artificially():
    a, b, n = map(int, input().split())
    if b > n:
        x = n
    else:
        x = b - 1
    print(int(a * x / b) - a * int(x / b))


if __name__ == "__main__":
    wrapped_artificially()
