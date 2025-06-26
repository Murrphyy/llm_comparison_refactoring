

def wrapped_artificially():
    N, K = map(int, input().split())
    A = list(map(lambda x: x - 1, map(int, input().split())))
    current = 0
    memo = {0: 0}
    for i in range(1, K + 1):
        current = A[current]
        if current in memo:
            length = i - memo[current]
            tmp = (K - memo[current]) % length
            for j in range(tmp):
                current = A[current]
            break
        else:
            memo[current] = i
    print(current + 1)


if __name__ == "__main__":
    wrapped_artificially()
