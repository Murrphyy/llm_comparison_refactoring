

def wrapped_artificially():
    n = int(input())
    a, b = map(int, input().split())
    for i in range(10000):
        if a <= n * i <= b:
            print('OK')
            break
    else:
        print('NG')


if __name__ == "__main__":
    wrapped_artificially()
