

def wrapped_artificially():
    n, k = map(int, input().split())
    ans = 0
    a = []
    for _ in range(n):
        a.append(0)
    for i in range(k):
        d = int(input())
        treat = list(map(int, input().split()))
        for snuke in treat:
            a[snuke - 1] += 1
    for j in range(n):
        if a[j] == 0:
            ans += 1
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
