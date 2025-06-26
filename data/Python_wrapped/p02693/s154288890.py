

def wrapped_artificially():
    k = int(input())
    a, b = map(int, input().split())
    cal = 0
    while cal <= b:
        if a <= cal <= b:
            print('OK')
            break
        else:
            cal += k
    if cal > b:
        print('NG')


if __name__ == "__main__":
    wrapped_artificially()
