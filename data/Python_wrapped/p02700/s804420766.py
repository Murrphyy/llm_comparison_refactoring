import sys
def input():
    return sys.stdin.readline().strip()
def mapint():
    return map(int, input().split())

def wrapped_artificially():
    sys.setrecursionlimit(10 ** 9)
    A, B, C, D = mapint()
    cnt = 0
    while 1:
        if cnt % 2 == 0:
            C -= B
        else:
            A -= D
        if C <= 0:
            print('Yes')
            break
        if A <= 0:
            print('No')
            break
        cnt += 1


if __name__ == "__main__":
    wrapped_artificially()
