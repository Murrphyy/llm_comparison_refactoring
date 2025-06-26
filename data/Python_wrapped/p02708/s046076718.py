from itertools import accumulate

def wrapped_artificially():
    mod = 10 ** 9 + 7
    n, k = map(int, input().split())
    arr = []
    for i in range(n + 1):
        arr.append(i)
    ls = [0] + list(accumulate(arr))
    ans = 0
    for i in range(k, n + 2):
        ans += (ls[-1] - ls[-1 - i] - ls[i] + 1) % mod
    ans %= mod
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
