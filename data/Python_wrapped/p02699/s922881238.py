

def wrapped_artificially():
    S, W = [int(i) for i in input().strip().split(' ')]
    if W >= S:
        print('unsafe')
    else:
        print('safe')


if __name__ == "__main__":
    wrapped_artificially()
