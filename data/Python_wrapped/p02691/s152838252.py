import sys
def input():
    return sys.stdin.readline().strip()
def mapint():
    return map(int, input().split())
from collections import Counter

def wrapped_artificially():
    sys.setrecursionlimit(10 ** 9)
    N = int(input())
    As = list(mapint())
    plus = [i + a for i, a in enumerate(As)]
    minus = [i - a for i, a in enumerate(As)]
    pc = Counter(plus)
    mc = Counter(minus)
    ans = 0
    for p, cnt in pc.most_common():
        ans += cnt * mc[p]
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
