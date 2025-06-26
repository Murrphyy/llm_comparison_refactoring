import math
import collections
def f(a, b, x):
    return math.floor(a * x / b) - a * math.floor(x / b)

def wrapped_artificially():
    a, b, n = map(int, input().split())
    dd = collections.defaultdict(int)
    print(f(a, b, min(b - 1, n)))


if __name__ == "__main__":
    wrapped_artificially()
