from math import ceil

def wrapped_artificially():
    A, B, C, D = map(int, input().split())
    E = ceil(C / B)
    F = ceil(A / D)
    print('Yes' if E <= F else 'No')


if __name__ == "__main__":
    wrapped_artificially()
