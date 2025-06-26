

def wrapped_artificially():
    N, M = map(int, input().split())
    Hs = list(map(int, input().split()))
    array = [[] for i in range(N)]
    array2 = list(range(1, N + 1))
    for i in range(M):
        a, b = map(int, input().split())
        array[a - 1].append(b)
        array[b - 1].append(a)
    z = list(zip(Hs, array, array2))
    z.sort(reverse=True)
    a, b, c = zip(*z)
    Hs2 = list(a)
    array = list(b)
    array2 = list(c)
    visited = [0] * N
    ans = 0
    for i in range(N):
        valid = True
        x = array2[i]
        for j in range(len(array[i])):
            visited[array[i][j] - 1] = 1
            if Hs[array[i][j] - 1] == Hs[x - 1]:
                valid = False
        if visited[x - 1] == 0 and valid:
            ans += 1
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
