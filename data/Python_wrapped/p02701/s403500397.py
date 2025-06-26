from math import *

def wrapped_artificially():
    n = int(input())
    a = []
    for i in range(n):
        s = input()
        a.append(s)
    s = set(a)
    print(len(s))


if __name__ == "__main__":
    wrapped_artificially()
