

def wrapped_artificially():
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    if sum(a) > N:
        print(-1)
    else:
        print(N - sum(a))


if __name__ == "__main__":
    wrapped_artificially()
