def modinv(a):
    if a == 1:
        return 1
    else:
        res = 1
        n = len(b)
        li = []
        for _ in range(n):
            li.append(a % mod)
            a = a * a % mod
        for item in blis:
            res = res * li[item] % mod
        return res

def wrapped_artificially():
    N, M, K = map(int, input().split())
    mod = 998244353
    b = str(bin(mod - 2))[2:]
    blis = []
    for _ in range(len(b)):
        if b[-_ - 1] == '1':
            blis.append(_)
    '      \ninv = [0,1]\nfor i in range(2, N):\n  inv.append((-inv[mod%i]*(mod//i))%mod)\n'
    if N == 1:
        print(M)
        exit()
    m = [1]
    s = 1
    for _ in range(N - 1):
        s = s * (M - 1) % mod
        m.append(s)
    ncombi = [1]
    c = 1
    for k in range(K):
        c = c * (N - 1 - k) * modinv(k + 1)
        c %= mod
        ncombi.append(c)
    '\nolis = ncombi\nfor k in range(N-1):\n  nlis = [1]\n  for  j in range(len(olis)-1):\n    nlis.append(olis[j]+olis[j+1])\n  nlis.append(1)\n  olis = nlis\n  #print(olis)\nncombi = olis\n'
    ans = 0
    for k in range(K + 1):
        ans = ans + m[-k - 1] * ncombi[k]
        ans %= mod
    ans = ans * M % mod
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
