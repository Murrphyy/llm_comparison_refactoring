

def wrapped_artificially():
    k = int(input())
    a, b = map(int, input().split())
    if b // k - (a - 1) // k > 0:
        print('OK')
    else:
        print('NG')


if __name__ == "__main__":
    wrapped_artificially()
