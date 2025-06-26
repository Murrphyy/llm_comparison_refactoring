import math

def wrapped_artificially():
    X = int(input())
    okane = 100
    year = 0
    while okane < X:
        okane = okane * 101 // 100
        year = year + 1
    print(year)


if __name__ == "__main__":
    wrapped_artificially()
