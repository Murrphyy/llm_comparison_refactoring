from collections import Counter

def wrapped_artificially():
    N = int(input())
    A = list(map(int, input().split()))
    s = [i + a for i, a in enumerate(A)]
    t = [j - a for j, a in enumerate(A)]
    d = Counter(s)
    ans = 0
    for i in t:
        ans += d[i]
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
