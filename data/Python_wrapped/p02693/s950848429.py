

def wrapped_artificially():
    k = int(input())
    a, b = map(int, input().split())
    print('OK' if b // k * k >= a else 'NG')


if __name__ == "__main__":
    wrapped_artificially()
