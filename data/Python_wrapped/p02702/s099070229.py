from collections import Counter

def wrapped_artificially():
    s = list(map(int, input()))
    s.reverse()
    t = len(s)
    mod = 2019
    arr = [0] * (t + 1)
    arr[-2] = s[0]
    for i in range(1, t):
        arr[t - i - 1] = (arr[t - i] + s[i] * pow(10, i, mod)) % mod
    arr = Counter(arr)
    ans = 0
    for i in arr:
        ans += (arr[i] - 1) * arr[i] // 2
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
