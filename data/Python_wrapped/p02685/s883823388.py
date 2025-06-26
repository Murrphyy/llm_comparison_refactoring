def cmb(n, m):
    return fact[n] * rfact[m] * rfact[n - m] % MOD

def wrapped_artificially():
    N, M, K = map(int, input().split())
    MOD = 998244353
    fact = [1]
    rfact = [1]
    for i in range(1, N + 1):
        fact.append(fact[i - 1] * i % MOD)
        rfact.append(pow(fact[i], MOD - 2, MOD))
    answer = 0
    for i in range(K + 1):
        answer += M * cmb(N - 1, i) * pow(M - 1, N - 1 - i, MOD) % MOD
    print(answer % MOD)


if __name__ == "__main__":
    wrapped_artificially()
