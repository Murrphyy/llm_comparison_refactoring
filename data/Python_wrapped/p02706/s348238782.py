

def wrapped_artificially():
    N, M = map(int, input().split())
    A = input().split()
    s = 0
    for i in range(M):
        s += int(A[i])
    ans = N - s
    if ans >= 0:
        print(ans)
    else:
        print('-1')


if __name__ == "__main__":
    wrapped_artificially()
