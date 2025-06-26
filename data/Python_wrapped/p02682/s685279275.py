

def wrapped_artificially():
    A, B, C, K = map(int, input().split())
    b = 0
    if A <= K:
        b = A
    elif A > K:
        b = K
    if A + B < K:
        b += -(K - A - B)
    print(b)


if __name__ == "__main__":
    wrapped_artificially()
