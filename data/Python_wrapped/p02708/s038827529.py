import sys
import itertools

def wrapped_artificially():
    N, K = map(int, input().split())
    a = 0
    h = 0
    l = 0
    for j in range(0, K - 1):
        h += j
    for j in range(N + 2 - K, N + 1):
        l += j
    for i in range(K, N + 2):
        h += i - 1
        l += N + 1 - i
        a += l - h + 1
    a %= 10 ** 9 + 7
    print(a)


if __name__ == "__main__":
    wrapped_artificially()
