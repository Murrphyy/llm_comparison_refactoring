

def wrapped_artificially():
    x = int(input())
    y = 100
    i = 0
    while x > y:
        y += y // 100
        i += 1
    print(i)


if __name__ == "__main__":
    wrapped_artificially()
