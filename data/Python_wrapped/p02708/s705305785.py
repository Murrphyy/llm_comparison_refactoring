

def wrapped_artificially():
    N, K = map(int, input().split())
    mod = 10 ** 9 + 7
    count = 0
    for n in range(K, N + 2):
        maxSum = n * (N + N - n + 1) // 2
        minSum = n * (n - 1) // 2
        count += maxSum - minSum + 1
        count %= mod
    print(count)


if __name__ == "__main__":
    wrapped_artificially()
