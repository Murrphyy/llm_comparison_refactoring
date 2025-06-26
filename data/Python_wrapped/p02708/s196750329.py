

def wrapped_artificially():
    N, K = map(int, input().split())
    mod = 10 ** 9 + 7
    print(((N + 1) * (N * N + 2 * N + 6) // 6 + (K - 1) * (2 * K * K - (3 * N + 4) * K - 6) // 6) % mod)


if __name__ == "__main__":
    wrapped_artificially()
