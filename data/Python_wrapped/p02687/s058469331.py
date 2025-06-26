import sys
def inp():
    return int(input())
def inps():
    return input().rstrip()
def inpl():
    return list(map(int, input().split()))
def _debug(obj):
    print(obj, file=sys.stderr)

def wrapped_artificially():
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 6)
    s = inps()
    print('ARC' if s == 'ABC' else 'ABC')


if __name__ == "__main__":
    wrapped_artificially()
