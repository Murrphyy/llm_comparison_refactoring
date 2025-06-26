def calc(x):
    return int(A * x / B) - A * int(x / B)

def wrapped_artificially():
    A, B, N = map(int, input().split())
    if N < B:
        print(calc(N))
    else:
        print(calc(B - 1))


if __name__ == "__main__":
    wrapped_artificially()
