

def wrapped_artificially():
    a, b, c, k = map(int, input().split())
    if k <= a:
        ans = k
    elif (a < k) & (k <= a + b):
        ans = a
    elif (a + b < k) & (k <= a + b + c):
        ans = a - (k - (a + b))
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
