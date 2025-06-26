import math
def fact(n):
    ans = 1
    for i in range(2, n + 1):
        ans *= i
    return ans
def comb(n, c):
    return fact(n) // (fact(n - c) * c)

def wrapped_artificially():
    n = int(input())
    nums = list(map(int, input().split()))
    ans = 0
    l = {}
    r = []
    for i in range(1, n + 1):
        if i + nums[i - 1] not in l:
            l[i + nums[i - 1]] = 0
        l[i + nums[i - 1]] += 1
        if -1 * nums[i - 1] + i in l:
            ans += l[-1 * nums[i - 1] + i]
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
