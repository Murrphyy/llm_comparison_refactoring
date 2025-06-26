from collections import Counter

def wrapped_artificially():
    N = int(input())
    A = list(map(int, input().split()))
    L = []
    for i in range(N):
        L.append(i - A[i])
    R = []
    for j in range(N):
        R.append(j + A[j])
    LL = Counter(L)
    RR = Counter(R)
    ans = 0
    for k, v in RR.items():
        ans += v * LL[k]
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
