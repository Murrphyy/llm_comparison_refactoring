def resolve():
    A, B, N = map(int, input().split())
    if B <= N + 1:
        print(A * (B - 1) // B)
    else:
        print(A * N // B)

def wrapped_artificially():
    resolve()


if __name__ == "__main__":
    wrapped_artificially()
