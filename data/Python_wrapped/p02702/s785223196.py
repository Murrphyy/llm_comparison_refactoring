def combinations(n, k):
    if k < 0 or n < k:
        return 0
    else:
        return fac[n] * ifac[k] * ifac[n - k] % MOD

def wrapped_artificially():
    MAX = 600000
    MOD = int(1000000000.0) + 7
    fac = [0] * MAX
    ifac = [0] * MAX
    fac[0] = 1
    for i in range(1, MAX):
        fac[i] = fac[i - 1] * i % MOD
    ifac[MAX - 1] = pow(fac[MAX - 1], MOD - 2, MOD)
    for i in reversed(range(1, MAX)):
        ifac[i - 1] = ifac[i] * i % MOD
    MOD2 = 2019
    s = list(input())
    s.reverse()
    n = len(s)
    ans = 0
    lis = [0] * 2020
    x = 1
    cnt = 0
    lis[cnt] += 1
    for i in s:
        cnt += int(i) * x
        cnt %= MOD2
        lis[cnt] += 1
        x *= 10
        x %= MOD2
    for i in lis:
        ans += combinations(i, 2)
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
