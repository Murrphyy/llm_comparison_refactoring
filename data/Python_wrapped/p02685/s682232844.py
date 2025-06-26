def comb(n, k):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * finv[k] % mod * finv[n - k] % mod

def wrapped_artificially():
    n, m, k = map(int, input().split())
    mod = 998244353
    fac = [1] * (n + 1)
    finv = [1] * (n + 1)
    for i in range(1, n + 1):
        fac[i] = fac[i - 1] * i % mod
        finv[i] = pow(fac[i], mod - 2, mod)
    p = [1] * (n + 1)
    for i in range(1, n + 1):
        p[i] = p[i - 1] * (m - 1) % mod
    ans = 0
    for i in range(k + 1):
        ans += m * comb(n - 1, i) % mod * p[n - 1 - i] % mod
        ans %= mod
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
