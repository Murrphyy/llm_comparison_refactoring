

def wrapped_artificially():
    s, w = map(int, input().split())
    if s > w:
        print('safe')
    elif s <= w:
        print('unsafe')


if __name__ == "__main__":
    wrapped_artificially()
