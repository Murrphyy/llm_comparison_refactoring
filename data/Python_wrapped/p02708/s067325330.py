def sum_(i, j):
    return (a[i] + a[j]) * (j - i + 1) // 2

def wrapped_artificially():
    N, K = list(map(int, input().split()))
    a = [i for i in range(N + 1)]
    ans = 0
    for i in range(K, N + 2):
        min_ = sum_(0, i - 1)
        max_ = sum_(N - i + 1, N)
        ans += max_ - min_ + 1
        ans %= 10 ** 9 + 7
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
