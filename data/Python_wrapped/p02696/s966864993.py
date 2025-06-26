

def wrapped_artificially():
    A, B, N = map(int, input().split())
    if B == 1:
        print(0)
    else:
        N = min(N, B - 1)
        print(A * N // B)


if __name__ == "__main__":
    wrapped_artificially()
