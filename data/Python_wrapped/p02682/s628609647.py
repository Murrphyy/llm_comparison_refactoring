

def wrapped_artificially():
    A, B, C, K = map(int, input().split())
    if K < A + B:
        print(min(K, A))
    else:
        print(2 * A + B - K)


if __name__ == "__main__":
    wrapped_artificially()
