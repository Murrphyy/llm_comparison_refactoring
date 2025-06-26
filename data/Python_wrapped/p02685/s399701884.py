def nCk(n, k):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n - k] % mod) % mod

def wrapped_artificially():
    n, m, k = map(int, input().split())
    mod = 998244353
    MAX_N = n + 5
    fac = [1, 1] + [0] * MAX_N
    finv = [1, 1] + [0] * MAX_N
    inv = [0, 1] + [0] * MAX_N
    for i in range(2, MAX_N):
        fac[i] = fac[i - 1] * i % mod
        inv[i] = mod - inv[mod % i] * (mod // i) % mod
        finv[i] = finv[i - 1] * inv[i] % mod
    ans = 0
    for i in range(k + 1):
        ans += nCk(n - 1, i) * m * pow(m - 1, n - i - 1, mod)
        ans %= mod
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
