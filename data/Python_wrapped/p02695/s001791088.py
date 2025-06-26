

def wrapped_artificially():
    n, m, q = map(int, input().split())
    A = [0] * q
    B = [0] * q
    C = [0] * q
    D = [0] * q
    for i in range(q):
        a, b, c, d = map(int, input().split())
        A[i] = a
        B[i] = b
        C[i] = c
        D[i] = d
    walist = []
    for i in range(2 ** (n + m - 1)):
        if bin(i).count('1') == n:
            wa = 0
            seq = []
            value = 1
            for j in range(n + m - 1):
                if i >> j & 1 == 1:
                    seq += [value]
                else:
                    value += 1
            for k in range(q):
                if seq[B[k] - 1] - seq[A[k] - 1] == C[k]:
                    wa += D[k]
            walist += [wa]
    print(max(walist))


if __name__ == "__main__":
    wrapped_artificially()
