def floor(x):
    return int(A * x / B) - A * int(x / B)

def wrapped_artificially():
    A, B, N = map(int, input().split())
    print(floor(min(B - 1, N)))


if __name__ == "__main__":
    wrapped_artificially()
