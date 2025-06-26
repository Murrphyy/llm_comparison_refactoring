import math

def wrapped_artificially():
    a, b, c, d = map(int, input().split(' '))
    taka = math.ceil(c / b)
    aoki = math.ceil(a / d)
    if taka <= aoki:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    wrapped_artificially()
