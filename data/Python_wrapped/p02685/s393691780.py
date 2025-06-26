def cmb(n, r):
    if r < 0 or r > n:
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % md
def cnt(k):
    ret = pow(M - 1, N - 1 - k, md)
    ret *= cmb(N - 1, k)
    ret %= md
    ret *= M
    ret %= md
    return ret
def main():
    rt = 0
    for k in range(K + 1):
        rt += cnt(k)
        rt %= md
    print(rt)

def wrapped_artificially():
    N, M, K = map(int, input().split())
    md = 998244353
    g1 = [1, 1]
    g2 = [1, 1]
    inverse = [0, 1]
    for i in range(2, N + 1):
        g1.append(g1[-1] * i % md)
        inverse.append(-inverse[md % i] * (md // i) % md)
        g2.append(g2[-1] * inverse[-1] % md)
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
