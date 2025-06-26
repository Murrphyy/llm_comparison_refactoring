from collections import defaultdict

def wrapped_artificially():
    N = int(input())
    X = list(map(int, input().split()))
    ctr = defaultdict(int)
    ans = 0
    for i in range(N):
        ctr[i + X[i]] += 1
        ans += ctr[i - X[i]]
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
