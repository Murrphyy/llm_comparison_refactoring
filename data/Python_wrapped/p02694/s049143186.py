import math

def wrapped_artificially():
    X = int(input())
    count = 0
    s = 100
    while s < X:
        s += s // 100
        count += 1
    print(count)


if __name__ == "__main__":
    wrapped_artificially()
