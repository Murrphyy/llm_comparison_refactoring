import math

def wrapped_artificially():
    A, B, C, D = map(int, input().split())
    t = math.ceil(C / B)
    a = math.ceil(A / D)
    print('Yes' if t <= a else 'No')


if __name__ == "__main__":
    wrapped_artificially()
