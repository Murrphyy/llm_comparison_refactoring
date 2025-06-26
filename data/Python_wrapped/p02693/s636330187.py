

def wrapped_artificially():
    k = int(input())
    a, b = map(int, input().split())
    count = 0
    for i in range(b - a + 1):
        if (i + a) % k == 0:
            print('OK')
            count += 1
            break
    if count == 0:
        print('NG')


if __name__ == "__main__":
    wrapped_artificially()
