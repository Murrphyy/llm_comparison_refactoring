

def wrapped_artificially():
    N, K = list(map(int, input().split()))
    C = 10 ** 9 + 7
    ans = 0
    A = sum(list(range(N, N - K, -1)))
    B = sum(list(range(K)))
    for i in range(K, N + 2):
        ans += A - B + 1
        A += N - i
        B += i
        ans %= C
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
