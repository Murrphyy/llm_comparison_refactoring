import sys
import os
def file_input():
    f = open('ABC167/input.txt', 'r')
    sys.stdin = f
def init_cmb(N, p):
    for i in range(2, N + 1):
        fact.append(fact[-1] * i % p)
        inv.append(-inv[p % i] * (p // i) % p)
        factinv.append(factinv[-1] * inv[-1] % p)
def cmb(n, r, p):
    if r < 0 or n < r:
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % p
def main():
    N, M, K = map(int, input().split())
    mod = 998244353
    ans = 0
    init_cmb(N, mod)
    for k in range(K + 1):
        ans += M * cmb(N - 1, k, mod) * pow(M - 1, N - 1 - k, mod)
    print(ans % mod)

def wrapped_artificially():
    fact = [1, 1]
    factinv = [1, 1]
    inv = [0, 1]
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
