import math

def wrapped_artificially():
    N, K = map(int, input().split())
    sum = 0
    for i in range(K, N + 2):
        sum += N * (N + 1) // 2 - (N - i) * (N - i + 1) // 2 - i * (i - 1) // 2 + 1
        sum %= 10 ** 9 + 7
    print(sum % (10 ** 9 + 7))


if __name__ == "__main__":
    wrapped_artificially()
