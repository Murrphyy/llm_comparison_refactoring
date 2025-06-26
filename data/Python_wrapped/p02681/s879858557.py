import sys

def wrapped_artificially():
    input = sys.stdin.readline
    ins = lambda: input().rstrip()
    ini = lambda: int(input().rstrip())
    inm = lambda: map(int, input().split())
    inl = lambda: list(map(int, input().split()))
    out = lambda x: print('\n'.join(map(str, x)))
    s = ins()
    t = ins()
    print('Yes' if s == t[:-1] else 'No')


if __name__ == "__main__":
    wrapped_artificially()
