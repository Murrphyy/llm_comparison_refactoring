import math

def wrapped_artificially():
    a, b, n = map(int, input().split())
    if n < b:
        ans = math.floor(a * n / b)
    else:
        ans = math.floor(a * (b - 1) / b)
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
