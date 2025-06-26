

def wrapped_artificially():
    x, y, z, w = map(int, input().split())
    while 1:
        if z > 0:
            z -= y
        if z <= 0:
            print('Yes')
            exit()
        if x > 0:
            x = x - w
        if x <= 0:
            print('No')
            exit()


if __name__ == "__main__":
    wrapped_artificially()
