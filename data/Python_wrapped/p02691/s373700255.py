from sys import stdin
from collections import Counter

def wrapped_artificially():
    nii = lambda: map(int, stdin.readline().split())
    lnii = lambda: list(map(int, stdin.readline().split()))
    n = int(input())
    a = lnii()
    l1 = [i + a[i] for i in range(n)]
    l2 = [i - a[i] for i in range(n)]
    c1 = Counter(l1)
    c2 = Counter(l2)
    ans = 0
    for i in c1:
        ans += c1[i] * c2[i]
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
