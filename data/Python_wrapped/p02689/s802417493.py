

def wrapped_artificially():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    ans = [1] * N
    for i in range(M):
        A, B = map(int, input().split())
        x = H[A - 1]
        y = H[B - 1]
        if x > y:
            ans[B - 1] = 0
        elif x == y:
            ans[B - 1] = 0
            ans[A - 1] = 0
        elif y > x:
            ans[A - 1] = 0
    print(sum(ans))


if __name__ == "__main__":
    wrapped_artificially()
