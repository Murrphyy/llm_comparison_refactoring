import math

def wrapped_artificially():
    X = int(input())
    deposit = 100
    year = 0
    while deposit < X:
        deposit = deposit + deposit // 100
        year += 1
    print(year)


if __name__ == "__main__":
    wrapped_artificially()
