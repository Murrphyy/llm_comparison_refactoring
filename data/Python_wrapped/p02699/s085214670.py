

def wrapped_artificially():
    S, W = map(int, input().split())
    print('safe' if W < S else 'unsafe')


if __name__ == "__main__":
    wrapped_artificially()
