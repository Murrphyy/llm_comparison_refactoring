

def wrapped_artificially():
    A, B, N = list(map(int, input().rstrip().split()))
    x = min(B - 1, N)
    calc = int(A * x / B) - A * int(x / B)
    print(calc)


if __name__ == "__main__":
    wrapped_artificially()
