import sys
from itertools import chain
def solve(N: int, S: 'List[str]'):
    return len(set(S))
def main():
    tokens = chain(*(line.split() for line in sys.stdin))
    N = int(next(tokens))
    S = [next(tokens) for _ in range(N)]
    answer = solve(N, S)
    print(answer)

def wrapped_artificially():
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
