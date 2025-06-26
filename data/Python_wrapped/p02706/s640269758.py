

def wrapped_artificially():
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = sum(a)
    if b > N:
        print(-1)
    elif b <= N:
        print(N - b)


if __name__ == "__main__":
    wrapped_artificially()
