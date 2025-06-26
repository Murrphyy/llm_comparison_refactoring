

def wrapped_artificially():
    k, a, b = map(int, open(0).read().split())
    print('OK' if b // k * k >= a else 'NG')


if __name__ == "__main__":
    wrapped_artificially()
