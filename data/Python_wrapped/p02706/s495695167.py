

def wrapped_artificially():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(M):
        sum += A[i]
    if N - sum >= 0:
        print(N - sum)
    else:
        print('-1')


if __name__ == "__main__":
    wrapped_artificially()
