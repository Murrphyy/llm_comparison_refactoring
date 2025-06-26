

def wrapped_artificially():
    A, B, N = map(int, input().split())
    x = 0
    if B > N:
        x = N
    else:
        x = B - 1
    print(A * x // B)


if __name__ == "__main__":
    wrapped_artificially()
