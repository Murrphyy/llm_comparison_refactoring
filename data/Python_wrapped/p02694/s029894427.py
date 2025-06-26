import sys
import time
import math
import itertools as it
def inp():
    return int(input())
def inpl():
    return list(map(int, input().split()))

def wrapped_artificially():
    read = sys.stdin.readline
    start_time = time.perf_counter()
    X = inp()
    yen = 100
    for i in range(10 ** 4):
        yen += yen // 100
        if yen >= X:
            print(i + 1)
            break
    end_time = time.perf_counter()
    print('time:', end_time - start_time, file=sys.stderr)


if __name__ == "__main__":
    wrapped_artificially()
