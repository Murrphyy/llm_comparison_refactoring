import sys

def wrapped_artificially():
    input = lambda: sys.stdin.readline().rstrip()
    sys.setrecursionlimit(max(1000, 10 ** 9))
    write = lambda x: sys.stdout.write(x + '\n')
    n = int(input())
    a = [None] * n
    for i in range(n):
        a[i] = input()
    s = set(a)
    print(len(s))


if __name__ == "__main__":
    wrapped_artificially()
