from collections import Counter

def wrapped_artificially():
    n = int(input())
    A = list(map(int, input().split()))
    ma = max(A) + n - 1
    P = [i + a + 1 for i, a in enumerate(A) if i + a + 1 <= ma]
    Q = [j - a + 1 for j, a in enumerate(A) if j - a + 1 > 0]
    cQ = Counter(Q)
    cP = Counter(P)
    ans = 0
    for p in cP.keys():
        ans += cQ[p] * cP[p]
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
