import sys

def wrapped_artificially():
    input = iter(sys.stdin.read().splitlines()).__next__
    sys.setrecursionlimit(10000)
    S = input()
    print('ARC' if S == 'ABC' else 'ABC')


if __name__ == "__main__":
    wrapped_artificially()
