import sys
def mi():
    return map(int, input().split())
def ii():
    return int(input())
def isp():
    return input().split()
def deb(text):
    print('-------\n{}\n-------'.format(text))
def main():
    K = ii()
    A, B = mi()
    for x in range(A, B + 1):
        if x % K == 0:
            print('OK')
            exit()
    print('NG')

def wrapped_artificially():
    sys.setrecursionlimit(10 ** 9)
    INF = 10 ** 20
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
