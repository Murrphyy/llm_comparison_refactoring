

def wrapped_artificially():
    K = int(input())
    A, B = map(int, input().split())
    C = A % K
    if B - A >= K - 1:
        print('OK')
    elif C == 0:
        print('OK')
    elif C + B - A >= K:
        print('OK')
    else:
        print('NG')


if __name__ == "__main__":
    wrapped_artificially()
