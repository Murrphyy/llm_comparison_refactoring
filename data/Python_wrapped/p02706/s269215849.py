def answer(N: int, M: int, A: list) -> int:
    homework_days = 0
    for i in range(0, M):
        homework_days += int(A[i])
        i += 1
    if homework_days <= N:
        return N - homework_days
    else:
        return -1

def wrapped_artificially():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    print(answer(N, M, A))


if __name__ == "__main__":
    wrapped_artificially()
