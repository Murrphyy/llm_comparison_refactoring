import numpy as np

def wrapped_artificially():
    n, k = map(int, input().split())
    ary = np.array([i for i in range(n + 1)])
    cum = np.cumsum(ary)
    ans = 0
    for j in range(k, n + 1):
        ans += cum[-1] - cum[-j - 1] - cum[j - 1] + 1
    else:
        ans += 1
        ans %= 10 ** 9 + 7
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
