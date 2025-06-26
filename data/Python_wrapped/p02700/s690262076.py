def ans(a, b, c, d):
    while 1:
        c -= b
        if c <= 0:
            return 'Yes'
        a -= d
        if a <= 0:
            return 'No'

def wrapped_artificially():
    a, b, c, d = map(int, input().split())
    print(ans(a, b, c, d))


if __name__ == "__main__":
    wrapped_artificially()
