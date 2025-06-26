

def wrapped_artificially():
    mod = 10 ** 9 + 7
    x = [0] + [0]
    for i in range(1, 2 * 10 ** 5 + 10):
        x.append((x[-1] + i) % mod)
    ans = 0
    n, k = map(int, input().split())
    for i in range(k, n + 2):
        ans += i * (n + n + 1 - i) // 2 - x[i] + 1
        ans %= mod
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
