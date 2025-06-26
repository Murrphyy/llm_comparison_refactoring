

def wrapped_artificially():
    A, B, C, K = [int(i) for i in input().split(' ')]
    print(min(A, K) - max(K - B - A, 0))


if __name__ == "__main__":
    wrapped_artificially()
