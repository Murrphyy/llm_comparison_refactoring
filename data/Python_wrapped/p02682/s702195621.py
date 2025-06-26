

def wrapped_artificially():
    A, B, C, K = map(int, input().split())
    sum = 0
    x = K - A
    if x > 0:
        sum += A
    else:
        sum += K
    x = x - B
    if x > 0:
        sum -= x
    print(sum)


if __name__ == "__main__":
    wrapped_artificially()
