

def wrapped_artificially():
    a, b, c, k = map(int, input().split())
    if k <= a:
        print(k)
    elif a < k <= a + b:
        print(a)
    elif a + b <= k:
        print(a * 2 - k + b)


if __name__ == "__main__":
    wrapped_artificially()
