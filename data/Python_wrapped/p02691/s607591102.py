from collections import defaultdict

def wrapped_artificially():
    N = int(input())
    A = list(map(int, input().split()))
    d = defaultdict(int)
    for i, a in enumerate(A):
        d[i + a] += 1
    ans = 0
    for j, a in enumerate(A):
        ans += d[j - a]
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
