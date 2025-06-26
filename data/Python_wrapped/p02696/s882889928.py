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
    A, B, N = mi()
    x = min(B - 1, N)
    f = A * x // B - A * (x // B)
    print(f)

def wrapped_artificially():
    sys.setrecursionlimit(10 ** 9)
    INF = 10 ** 20
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
