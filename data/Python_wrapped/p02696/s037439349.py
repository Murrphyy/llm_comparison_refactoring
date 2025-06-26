import math

def wrapped_artificially():
    A, B, N = map(int, input().split())
    n = min(N, B - 1)
    print(math.floor(A * n / B))


if __name__ == "__main__":
    wrapped_artificially()
