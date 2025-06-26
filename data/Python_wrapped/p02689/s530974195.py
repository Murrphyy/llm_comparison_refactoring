

def wrapped_artificially():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    ma = [0] * N
    for i in range(M):
        A, B = map(int, input().split())
        A -= 1
        B -= 1
        ma[A] = max(ma[A], H[B])
        ma[B] = max(ma[B], H[A])
    ans = 0
    for i in range(N):
        if H[i] > ma[i]:
            ans += 1
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
