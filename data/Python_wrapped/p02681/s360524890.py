

def wrapped_artificially():
    s, t = (input(), input())
    print('Yes' if s == t[:-1] else 'No')


if __name__ == "__main__":
    wrapped_artificially()
