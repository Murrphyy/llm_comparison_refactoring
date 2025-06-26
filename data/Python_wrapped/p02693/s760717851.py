import math

def wrapped_artificially():
    k = int(input())
    a, b = map(int, input().split())
    if k == 1:
        print('OK')
        exit()
    elif a <= k <= b:
        print('OK')
        exit()
    cnt = 1
    while True:
        tmp = cnt * k
        if a <= tmp <= b:
            print('OK')
            exit()
        elif b <= tmp:
            print('NG')
            exit()
        cnt += 1


if __name__ == "__main__":
    wrapped_artificially()
