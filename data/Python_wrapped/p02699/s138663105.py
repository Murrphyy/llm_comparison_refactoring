

def wrapped_artificially():
    S, W = list(map(int, input().split()))
    if W >= S:
        print('unsafe')
    else:
        print('safe')


if __name__ == "__main__":
    wrapped_artificially()
