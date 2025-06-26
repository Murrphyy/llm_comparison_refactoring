

def wrapped_artificially():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    Flags = [1] * N
    cnt = N
    for _ in range(M):
        A, B = map(int, input().split())
        if H[A - 1] <= H[B - 1] and Flags[A - 1]:
            cnt -= 1
            Flags[A - 1] = 0
        if H[A - 1] >= H[B - 1] and Flags[B - 1]:
            cnt -= 1
            Flags[B - 1] = 0
    print(cnt)


if __name__ == "__main__":
    wrapped_artificially()
