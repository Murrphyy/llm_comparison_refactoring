

def wrapped_artificially():
    n, k = [int(i) for i in input().split()]
    m = n + 2 - k
    a = -m * (m + 1) * (2 * m + 1) // 6
    b = (n - 2 * k + 3) * m * (m + 1) // 2
    c = m * (-k ** 2 + 3 * k + n * k - n - 1)
    mod = 10 ** 9 + 7
    a = a % mod
    b = b % mod
    c = c % mod
    ans = a + b + c
    print(ans % mod)


if __name__ == "__main__":
    wrapped_artificially()
