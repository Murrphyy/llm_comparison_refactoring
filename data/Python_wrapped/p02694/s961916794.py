

def wrapped_artificially():
    a = int(input())
    count = 0
    x = 100
    while True:
        if x >= a:
            break
        x += x // 100
        count += 1
    print(count)


if __name__ == "__main__":
    wrapped_artificially()
