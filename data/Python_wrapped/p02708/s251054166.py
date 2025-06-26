

def wrapped_artificially():
    n, k = map(int, input().split())
    s = 0
    for i in range(k, n + 2):
        s += i * (n * 2 + 1 - i) // 2 - i * (i - 1) // 2 + 1
    print(s % 1000000007)


if __name__ == "__main__":
    wrapped_artificially()
