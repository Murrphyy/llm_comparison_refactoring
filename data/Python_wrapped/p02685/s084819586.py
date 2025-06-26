def nCk(n, k):
    return fact[n] * pow(fact[n - k] * fact[k], mod - 2, mod)

def wrapped_artificially():
    N, M, K = map(int, input().split())
    mod = 998244353
    fact = [1 for i in range(N + 1)]
    for i in range(1, N):
        fact[i + 1] = fact[i] * (i + 1) % mod
    result = 0
    for k in range(K + 1):
        result += nCk(N - 1, k) * M * pow(M - 1, N - k - 1, mod)
        result = int(result) % mod
    print(result)


if __name__ == "__main__":
    wrapped_artificially()
