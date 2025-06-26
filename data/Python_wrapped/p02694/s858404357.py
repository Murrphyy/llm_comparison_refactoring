

def wrapped_artificially():
    x = int(input())
    n = 100
    y = 0
    while n < x:
        n = n * 101 // 100
        y += 1
    print(y)


if __name__ == "__main__":
    wrapped_artificially()
