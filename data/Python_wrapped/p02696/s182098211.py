import sys
from collections import deque
import copy
import math
def main():
    A, B, N = map(int, input().split())
    if B - 1 <= N:
        x = B - 1
    else:
        x = N
    ans = math.floor(A * x / B) - A * math.floor(x / B)
    print(ans)

def wrapped_artificially():
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
