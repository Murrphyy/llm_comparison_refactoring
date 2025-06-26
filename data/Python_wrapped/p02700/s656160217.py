import math

def wrapped_artificially():
    A, B, C, D = map(int, input().split())
    E = math.ceil(A / D)
    F = math.ceil(C / B)
    if E >= F:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    wrapped_artificially()
