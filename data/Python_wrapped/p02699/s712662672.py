

def wrapped_artificially():
    s, w = map(int, input().split())
    print('safe' if w < s else 'unsafe')


if __name__ == "__main__":
    wrapped_artificially()
