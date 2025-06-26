import sys

def wrapped_artificially():
    input = sys.stdin.readline
    K = int(input())
    A, B = list(map(int, input().split()))
    flag = 0
    for i in range(A, B + 1):
        if i % K == 0:
            flag = 1
    print('OK' if flag == 1 else 'NG')


if __name__ == "__main__":
    wrapped_artificially()
