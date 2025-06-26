import math

def wrapped_artificially():
    k = int(input())
    [a, b] = list(map(int, input().split()))
    A = math.floor(a / k)
    B = math.floor(b / k)
    if A != B:
        print('OK')
    elif k == 1:
        print('OK')
    elif a % k == 0 or b % k == 0:
        print('OK')
    else:
        print('NG')


if __name__ == "__main__":
    wrapped_artificially()
