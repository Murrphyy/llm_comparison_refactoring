def nCr(n, r, fac, finv):
    mod = 998244353
    ans = fac[n] * (finv[r] * finv[n - r] % mod) % mod
    return ans

def wrapped_artificially():
    n, m, k = map(int, input().split())
    ans = 0
    mod = 998244353
    fac = [1, 1] + [0] * n
    finv = [1, 1] + [0] * n
    inv = [1, 1] + [0] * n
    for i in range(2, n + 1):
        fac[i] = fac[i - 1] * i % mod
        inv[i] = mod - inv[mod % i] * (mod // i) % mod
        finv[i] = finv[i - 1] * inv[i] % mod
    for i in range(k + 1):
        ans += m * pow(m - 1, n - 1 - i, mod) * nCr(n - 1, i, fac, finv) % mod
        ans %= mod
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
