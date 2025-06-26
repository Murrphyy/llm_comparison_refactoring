

def wrapped_artificially():
    a, b, n = map(int, input().split())
    t = min(b - 1, n)
    ans = a * t // b - a * (t // b)
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
