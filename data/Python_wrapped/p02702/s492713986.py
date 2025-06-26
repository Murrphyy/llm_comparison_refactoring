import collections

def wrapped_artificially():
    s = input()
    mod = 2019
    n = len(s)
    t = [0] * (n + 1)
    for i in range(1, n + 1):
        t[i] = (t[i - 1] + int(s[n - i]) * pow(10, i - 1, mod)) % mod
    c = collections.Counter(t)
    num = c.values()
    ans = 0
    for i in num:
        ans += i * (i - 1) // 2
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
