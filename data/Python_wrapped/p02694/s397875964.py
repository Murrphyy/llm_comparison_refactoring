

def wrapped_artificially():
    X = int(input().split()[0])
    x = 100
    count = 0
    while x < X:
        x += x // 100
        count += 1
    ans = count
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
