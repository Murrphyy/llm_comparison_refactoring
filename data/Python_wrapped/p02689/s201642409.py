

def wrapped_artificially():
    n, m = map(int, input().split())
    H = list(map(int, input().split()))
    a = [list(map(int, input().split())) for _ in range(m)]
    flag = [0] * n
    for i in range(m):
        if H[a[i][0] - 1] > H[a[i][1] - 1]:
            flag[a[i][1] - 1] = 2
        elif H[a[i][0] - 1] == H[a[i][1] - 1]:
            flag[a[i][0] - 1] = 2
            flag[a[i][1] - 1] = 2
        else:
            flag[a[i][0] - 1] = 2
    cnt = 0
    for j in range(n):
        if flag[j] == 0:
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    wrapped_artificially()
