

def wrapped_artificially():
    a, b, c, d = [int(x) for x in input().split()]
    while True:
        if c - b <= 0:
            print('Yes')
            break
        else:
            c -= b
        if a - d <= 0:
            print('No')
            break
        else:
            a -= d


if __name__ == "__main__":
    wrapped_artificially()
