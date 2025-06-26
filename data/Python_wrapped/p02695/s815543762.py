def dfs(A):
    if len(A) == N:
        tmp = 0
        for a, b, c, d in arr:
            if A[b - 1] - A[a - 1] == c:
                tmp += d
        target.append(tmp)
        return
    start = 1
    if len(A) != 0:
        start = A[-1]
    for v in range(start, M + 1):
        A.append(v)
        dfs(A)
        A.pop()

def wrapped_artificially():
    target = []
    N, M, Q = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(Q)]
    dfs([])
    print(max(target))


if __name__ == "__main__":
    wrapped_artificially()
