def solve(*args: str) -> str:
    n, m, k = map(int, args[0].split())
    mod = 998244353
    if m == 1 and n - 1 == k:
        return str(1)
    iR = [1]
    C = [1]
    for i in range(1, k + 1):
        iR.append(max(1, -(mod // i) * iR[mod % i] % mod))
        C.append((n - i) * C[i - 1] * iR[i] % mod)
    ret = 0
    p = m * pow(m - 1, n - 1 - k, mod) % mod
    for i in range(1, k + 1):
        ret += p * C[-i] % mod
        p = p * (m - 1) % mod
    ret += p
    return str(ret % mod)

def wrapped_artificially():
    if __name__ == '__main__':
        print(solve(*open(0).read().splitlines()))


if __name__ == "__main__":
    wrapped_artificially()
