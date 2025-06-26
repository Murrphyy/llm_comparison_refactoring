import math

def wrapped_artificially():
    X = int(input())
    price = 100
    count = 0
    while price < X:
        tax = price // 100
        price += tax
        count += 1
    print(count)


if __name__ == "__main__":
    wrapped_artificially()
