

def wrapped_artificially():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    w = sum(A)
    ans = N - w
    if ans >= 0:
        print(ans)
    else:
        print(-1)


if __name__ == "__main__":
    wrapped_artificially()
