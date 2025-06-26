import sys
def comb(n, r, p):
    if r < 0 or n < r:
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % p

def wrapped_artificially():
    stdin = sys.stdin
    ns = lambda: stdin.readline().rstrip()
    ni = lambda: int(stdin.readline().rstrip())
    nm = lambda: map(int, stdin.readline().split())
    nl = lambda: list(map(int, stdin.readline().split()))
    p = 998244353
    N, M, K = nm()
    fact = [1, 1]
    factinv = [1, 1]
    inv = [0, 1]
    for i in range(2, N):
        fact.append(fact[-1] * i % p)
        inv.append(-inv[p % i] * (p // i) % p)
        factinv.append(factinv[-1] * inv[-1] % p)
    mod_M = [1, (M - 1) % p]
    for i in range(2, N):
        mod_M.append(mod_M[i - 1] * (M - 1) % p)
    ans = 0
    ans += M * mod_M[N - 1] % p
    if K > 0:
        for i in range(1, K + 1):
            ans += M * mod_M[N - i - 1] % p * comb(N - 1, i, p)
            ans %= p
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
