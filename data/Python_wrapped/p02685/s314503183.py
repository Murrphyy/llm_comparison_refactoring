

def wrapped_artificially():
    n, m, k = map(int, input().split())
    mod = 998244353
    ans = 0
    num = n
    fact = [0] * num
    fact[0] = 1
    for i in range(1, num):
        fact[i] = fact[i - 1] * i % mod
    M_pow = [0] * num
    M_pow[0] = 1
    for i in range(1, num):
        M_pow[i] = M_pow[i - 1] * (m - 1) % mod
    for i in range(k + 1):
        f = M_pow[n - i - 1] * pow(fact[i] * fact[n - i - 1], mod - 2, mod)
        ans += f % mod
    ans *= m * fact[n - 1]
    print(ans % mod)


if __name__ == "__main__":
    wrapped_artificially()
