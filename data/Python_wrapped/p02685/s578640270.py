def comb(n, k, nk, mod):
    return n * pow(k * nk, mod - 2, mod) % mod
def main():
    n, m, k = map(int, input().split())
    mod = 998244353
    ans = 0
    base = pow(m - 1, n - 1 - k, mod)
    fact = [1 for _ in range(n + 1)]
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i
        fact[i] %= mod
    for i in range(k, -1, -1):
        ans += base * comb(fact[n - 1], fact[i], fact[n - i - 1], mod)
        ans %= mod
        base *= m - 1
        base %= mod
    ans *= m
    ans %= mod
    print(ans)

def wrapped_artificially():
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
