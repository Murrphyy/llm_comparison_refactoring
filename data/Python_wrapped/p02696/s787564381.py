import math
def f(A, B, x):
    return math.floor(A * x / B) - A * math.floor(x / B)

def wrapped_artificially():
    A, B, N = map(int, input().split())
    x = min(N, B - 1)
    print(f(A, B, x))


if __name__ == "__main__":
    wrapped_artificially()
