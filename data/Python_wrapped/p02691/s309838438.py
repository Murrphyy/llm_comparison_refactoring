

def wrapped_artificially():
    n = int(input())
    a = list(map(int, input().split()))
    memo = {}
    ans = 0
    for i in range(n):
        diff = i - a[i]
        memo.setdefault(diff, 0)
        ans += memo[diff]
        sum = a[i] + i
        memo.setdefault(sum, 0)
        memo[sum] += 1
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
