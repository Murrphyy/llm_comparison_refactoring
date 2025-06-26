

def wrapped_artificially():
    x = int(input())
    money = 100
    cnt = 0
    while x > money:
        money += money // 100
        cnt += 1
    print(cnt)


if __name__ == "__main__":
    wrapped_artificially()
