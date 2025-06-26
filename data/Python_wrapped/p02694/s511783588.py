

def wrapped_artificially():
    a, year = (100, 0)
    x = int(input())
    while a < x:
        a += a // 100
        year += 1
    print(year)


if __name__ == "__main__":
    wrapped_artificially()
