import math

def wrapped_artificially():
    X = int(input())
    now = 100
    year = 0
    while True:
        if now >= X:
            break
        now += now // 100
        year += 1
    print(year)


if __name__ == "__main__":
    wrapped_artificially()
