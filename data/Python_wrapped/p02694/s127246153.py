def main():
    X = int(input())
    cnt = 0
    money = 100
    while money < X:
        cnt += 1
        money = money * 101
        money //= 100
    return cnt

def wrapped_artificially():
    print(main())


if __name__ == "__main__":
    wrapped_artificially()
