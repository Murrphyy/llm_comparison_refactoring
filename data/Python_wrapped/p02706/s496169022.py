

def wrapped_artificially():
    N, M = map(int, input().split())
    l = list(map(int, input().split()))
    total = 0
    for k in range(M):
        total += l[k]
    if total <= N:
        print(N - total)
    else:
        print('-1')


if __name__ == "__main__":
    wrapped_artificially()
