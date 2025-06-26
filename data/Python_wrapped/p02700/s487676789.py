

def wrapped_artificially():
    a, b, c, d = map(int, input().split())
    for i in range(200):
        if i % 2 == 0:
            c -= b
        else:
            a -= d
        if a <= 0:
            print('No')
            break
        elif c <= 0:
            print('Yes')
            break


if __name__ == "__main__":
    wrapped_artificially()
