

def wrapped_artificially():
    A, B, C, K = map(int, input().split())
    if K > A + B:
        s = A - (K - A - B)
    else:
        s = min(A, K)
    print(s)


if __name__ == "__main__":
    wrapped_artificially()
