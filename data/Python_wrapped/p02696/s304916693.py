

def wrapped_artificially():
    a, b, n = map(int, input().split())
    score = 0
    if n < b:
        print(int(a * n / b))
    elif b == 1:
        print(0)
    else:
        c = int(n / b)
        score = 0
        for i in range(1, c + 1):
            n_ = b * i - 1
            t = int(a * n_ / b) - a * int(n_ / b)
            score = max(score, t)
        t = int(a * n / b) - a * int(n / b)
        score = max(score, t)
        print(score)


if __name__ == "__main__":
    wrapped_artificially()
