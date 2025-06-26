

def wrapped_artificially():
    k = int(input())
    a, b = map(int, input().split(' '))
    flag = 0
    for i in range(a, b + 1):
        if i % k == 0:
            flag = 1
    if flag == 1:
        print('OK')
    else:
        print('NG')


if __name__ == "__main__":
    wrapped_artificially()
