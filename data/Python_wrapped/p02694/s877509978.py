

def wrapped_artificially():
    x = int(input())
    mon = 100
    cnt = 0
    while mon < x:
        mon += mon // 100
        cnt += 1
    print(cnt)


if __name__ == "__main__":
    wrapped_artificially()
