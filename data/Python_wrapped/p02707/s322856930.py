from typing import *
import collections
import itertools
import math
import sys
def solve(N: int, A: 'List[int]'):
    c = collections.Counter(A + [i + 1 for i in range(N)])
    return '\n'.join([f'{c[i + 1] - 1}' for i in range(N)])
def main():
    sys.setrecursionlimit(10 ** 6)

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    A = [int(next(tokens)) for _ in range(N - 2 + 1)]
    print(solve(N, A))

def wrapped_artificially():
    INF = float('inf')
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
