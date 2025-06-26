def resolve():
    N, K = map(int, input().split())
    D = []
    A = []
    for _ in range(K):
        d = int(input())
        a = list(map(int, input().split()))
        D.append(d)
        A.append(a)
    ans = 0
    for i in range(N):
        flag = 0
        for j in range(K):
            if i + 1 in A[j]:
                flag = 1
        if flag == 0:
            ans += 1
    print(ans)

def wrapped_artificially():
    resolve()


if __name__ == "__main__":
    wrapped_artificially()
