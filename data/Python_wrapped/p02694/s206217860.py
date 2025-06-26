import math

def wrapped_artificially():
    X = int(input())
    a = 100
    for i in range(1, 200000):
        a += a // 100
        if a >= X:
            break
    print(i)


if __name__ == "__main__":
    wrapped_artificially()
