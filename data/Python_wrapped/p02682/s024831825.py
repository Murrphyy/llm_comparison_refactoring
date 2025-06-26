

def wrapped_artificially():
    a, b, c, k = map(int, input().split())
    ans = 0
    if a > k:
        print(k)
    elif a + b > k:
        print(a)
    else:
        print(a - (k - a - b))


if __name__ == "__main__":
    wrapped_artificially()
