from math import ceil

def wrapped_artificially():
    a, b, c, d = map(int, input().split())
    x = ceil(c / b)
    y = ceil(a / d)
    if x <= y:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    wrapped_artificially()
