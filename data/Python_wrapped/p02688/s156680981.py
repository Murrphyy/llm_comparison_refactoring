def resolve():
    N, K = list(map(int, input().split()))
    snacks = [0 for _ in range(N)]
    for i in range(K):
        d = int(input())
        A = list(map(int, input().split()))
        for a in A:
            snacks[a - 1] += 1
    cnt = 0
    for s in snacks:
        if s == 0:
            cnt += 1
    print(cnt)

def wrapped_artificially():
    if '__main__' == __name__:
        resolve()


if __name__ == "__main__":
    wrapped_artificially()
