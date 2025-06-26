

def wrapped_artificially():
    n, K = list(map(int, input().split()))
    mod = 10 ** 9 + 7
    ans = 0
    for k in range(K, n + 2):
        ans += n * k - k ** 2 + k + 1
    print(ans % mod)


if __name__ == "__main__":
    wrapped_artificially()
