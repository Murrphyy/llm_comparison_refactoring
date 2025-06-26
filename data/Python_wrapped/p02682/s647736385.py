

def wrapped_artificially():
    a, b, c, k = map(int, input().split())
    print(min(a, k) - max(k - a - b, 0))


if __name__ == "__main__":
    wrapped_artificially()
