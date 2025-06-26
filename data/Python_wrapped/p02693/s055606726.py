

def wrapped_artificially():
    k = int(input())
    a, b = map(int, input().split())
    count = a
    while count <= b:
        if count % k == 0:
            print('OK')
            break
        else:
            count += 1
    else:
        print('NG')


if __name__ == "__main__":
    wrapped_artificially()
