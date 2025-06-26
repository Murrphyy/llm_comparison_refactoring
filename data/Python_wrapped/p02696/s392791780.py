

def wrapped_artificially():
    A, B, N = map(int, input().split())
    if N >= B:
        x = B - 1
    else:
        x = N
    '\nprint(x)\n'
    print(A * x // B - A * (x // B))


if __name__ == "__main__":
    wrapped_artificially()
