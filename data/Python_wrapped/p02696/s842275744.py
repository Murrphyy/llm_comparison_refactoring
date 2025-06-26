import sys
from sys import stdin
def input():
    return sys.stdin.readline().strip()
def I():
    return int(input())
def LI():
    return list(map(int, input().split()))
def IR(n):
    return [I() for i in range(n)]
def LIR(n):
    return [LI() for i in range(n)]
def SR(n):
    return [S() for i in range(n)]
def S():
    return input()
def LS():
    return input().split()

def wrapped_artificially():
    a, b, n = LI()
    x = b - 1 if b - 1 <= n else n
    print(int(a * x / b) - a * int(x / b))


if __name__ == "__main__":
    wrapped_artificially()
