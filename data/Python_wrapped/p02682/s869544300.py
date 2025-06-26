

def wrapped_artificially():
    a, b, c, k = map(int, input().split())
    sum = 0
    if a - k >= 0:
        sum += k
    else:
        sum += a
        if b - (k - a) >= 0:
            pass
        else:
            sum -= k - a - b
    print(sum)


if __name__ == "__main__":
    wrapped_artificially()
