

def wrapped_artificially():
    K = int(input())
    A, B = map(int, input().split())
    for i in range(1, 1000):
        if K * i > 1000:
            break
        if K * i >= A and K * i <= B:
            print('OK')
            exit()
    print('NG')


if __name__ == "__main__":
    wrapped_artificially()
