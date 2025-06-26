

def wrapped_artificially():
    N, K = map(int, input().split())
    upper = sum(range(N + 1))
    lower = sum(range(N + 1))
    answer = 1
    for k in range(N, K - 1, -1):
        upper -= N - k
        lower -= max(0, k)
        answer += upper - lower + 1
    print(answer % (10 ** 9 + 7))


if __name__ == "__main__":
    wrapped_artificially()
