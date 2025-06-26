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
    X = ii()
    i = 1
    yen = 100
    while yen < X:
        r = yen // 100
        yen += r
        i += 1
    print(i - 1)

def wrapped_artificially():
    sys.setrecursionlimit(10 ** 9)
    INF = 10 ** 20
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
