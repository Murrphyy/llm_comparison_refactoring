import sys
from collections import Counter

def wrapped_artificially():
    N = int(input())
    S = [str(s) for s in sys.stdin.read().split()]
    items = list(dict.fromkeys(S))
    print(len(items))


if __name__ == "__main__":
    wrapped_artificially()
