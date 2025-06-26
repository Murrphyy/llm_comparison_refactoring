import sys

def wrapped_artificially():
    sys.setrecursionlimit(10 ** 7)
    input = sys.stdin.readline
    s, w = map(int, input().split())
    if w >= s:
        print('unsafe')
    else:
        print('safe')


if __name__ == "__main__":
    wrapped_artificially()
