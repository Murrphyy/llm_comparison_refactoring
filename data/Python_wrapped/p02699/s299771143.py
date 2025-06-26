

def wrapped_artificially():
    S, W = map(int, input().split())
    if S <= W:
        print('unsafe')
    else:
        print('safe')


if __name__ == "__main__":
    wrapped_artificially()
