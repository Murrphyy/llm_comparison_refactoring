

def wrapped_artificially():
    N, K = map(int, input().split())
    c = 0
    for i in range(K, N + 2):
        min = i * (i + 1) / 2
        max = i * (N + 2 - i + N + 1) / 2
        c += max - min + 1
        c %= 1000000000.0 + 7
    print(int(c))


if __name__ == "__main__":
    wrapped_artificially()
