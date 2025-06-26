from math import floor

def wrapped_artificially():
    X = int(input())
    deposit, year = (100, 0)
    while deposit < X:
        deposit += deposit // 100
        year += 1
    print(year)


if __name__ == "__main__":
    wrapped_artificially()
