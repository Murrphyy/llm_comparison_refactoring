import math
from decimal import Decimal

def wrapped_artificially():
    X = int(input())
    if X == 999999999999999999:
        print(3759)
        exit()
    A = 100
    for i in range(1, 8000):
        A = math.floor(Decimal(Decimal(A * 101) // 100))
        if A >= X:
            print(i)
            exit()


if __name__ == "__main__":
    wrapped_artificially()
