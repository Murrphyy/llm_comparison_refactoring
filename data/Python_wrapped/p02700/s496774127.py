

def wrapped_artificially():
    a, b, c, d = map(int, input().split())
    while 1:
        c = c - b
        if c <= 0:
            print('Yes')
            exit()
        a = a - d
        if a <= 0:
            print('No')
            exit()


if __name__ == "__main__":
    wrapped_artificially()
