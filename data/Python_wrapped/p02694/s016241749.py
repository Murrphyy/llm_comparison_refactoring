

def wrapped_artificially():
    X = int(input())
    money = 100
    ans = 0
    while money < X:
        tax = money // 100
        money += tax
        ans += 1
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
