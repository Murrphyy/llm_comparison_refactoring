from collections import Counter

def wrapped_artificially():
    N = int(input())
    A = list(map(int, input().split()))
    B = Counter(list((i + 1 + A[i] for i in range(N))))
    C = Counter((i + 1 - A[i] for i in range(N)))
    ans = 0
    for j in range(N):
        ans += B[j] * C[j]
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
