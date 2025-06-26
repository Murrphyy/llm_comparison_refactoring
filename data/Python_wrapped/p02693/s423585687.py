

def wrapped_artificially():
    k = int(input())
    a, b = map(int, input().split())
    m = k
    while True:
        if a <= m <= b:
            print('OK')
            break
        m += k
        if m >= 1000:
            print('NG')
            break


if __name__ == "__main__":
    wrapped_artificially()
