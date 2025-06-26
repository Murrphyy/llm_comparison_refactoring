

def wrapped_artificially():
    e = enumerate
    n, *a = map(int, open(0).read().split())
    d = [0]
    for j, (a, i) in e(sorted(((a, i) for i, a in e(a)))[::-1]):
        d = [d[0] + a * (~i - j + n)] + [max(d[k + 1] + a * (n + k - i - j), d[k] + a * abs(i - k)) for k in range(j)] + [d[j] + a * abs(i - j)]
    print(max(d))


if __name__ == "__main__":
    wrapped_artificially()
