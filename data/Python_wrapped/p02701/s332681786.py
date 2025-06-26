import sys

def wrapped_artificially():
    N = int(input())
    S = [str(s) for s in sys.stdin.read().split()]
    print(len(set(S)))


if __name__ == "__main__":
    wrapped_artificially()
