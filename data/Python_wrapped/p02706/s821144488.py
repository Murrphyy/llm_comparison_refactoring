from typing import *
import itertools
import math
import sys
def solve(N: int, M: int, A: 'List[int]'):
    return max(N - sum(A), -1)
def main():
    sys.setrecursionlimit(10 ** 6)

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    M = int(next(tokens))
    A = [int(next(tokens)) for _ in range(M)]
    print(solve(N, M, A))

def wrapped_artificially():
    INF = float('inf')
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
