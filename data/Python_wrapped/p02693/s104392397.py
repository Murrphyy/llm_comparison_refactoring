

def wrapped_artificially():
    k = int(input())
    [a, b] = input().split()
    a = int(a)
    b = int(b)
    ans = False
    for i in range(a, b + 1):
        if i % k == 0:
            ans = True
            break
    if ans:
        print('OK')
    else:
        print('NG')


if __name__ == "__main__":
    wrapped_artificially()
