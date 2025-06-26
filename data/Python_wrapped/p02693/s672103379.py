

def wrapped_artificially():
    K = int(input())
    A, B = [int(i) for i in input().split()]
    f = False
    for i in range(A, B + 1):
        if i % K == 0:
            print('OK')
            f = True
            break
    if f is False:
        print('NG')


if __name__ == "__main__":
    wrapped_artificially()
