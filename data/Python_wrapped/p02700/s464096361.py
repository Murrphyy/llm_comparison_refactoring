import math

def wrapped_artificially():
    A, B, C, D = map(int, input().split())
    print('Yes') if math.ceil(A / D) >= math.ceil(C / B) else print('No')


if __name__ == "__main__":
    wrapped_artificially()
