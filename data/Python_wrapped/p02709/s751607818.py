

def wrapped_artificially():
    e = enumerate
    n, *a = map(int, open(0).read().split())
    d = [0]
    for j, (a, i) in e(sorted(((a, i) for i, a in e(a)))[::-1]):
        d = [d[0] + a * abs(n - j - i - 1)] + [max(d[k] + a * abs(n - j + k - i - 1), d[k - 1] + a * abs(i - k + 1)) for k in range(1, j + 1)] + [d[j] + a * abs(i - j)]
    print(max(d))


if __name__ == "__main__":
    wrapped_artificially()
