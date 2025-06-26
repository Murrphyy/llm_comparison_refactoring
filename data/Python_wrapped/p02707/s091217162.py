import sys
from itertools import chain
def solve(N: int, A: 'List[int]'):
    s = [0 for _ in range(N)]
    for Ai in A:
        s[Ai - 1] += 1
    return '\n'.join(map(str, s))
def main():
    tokens = chain(*(line.split() for line in sys.stdin))
    N = int(next(tokens))
    A = [int(next(tokens)) for _ in range(N - 2 + 1)]
    answer = solve(N, A)
    print(answer)

def wrapped_artificially():
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
