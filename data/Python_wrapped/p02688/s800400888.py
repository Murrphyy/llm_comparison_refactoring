

def wrapped_artificially():
    N, K = map(int, input().split())
    d = []
    A = []
    for i in range(K):
        temp_d = int(input())
        d.append(temp_d)
        temp_A = list(map(int, input().split()))
        A.append(temp_A)
    sum_A = []
    for i in range(K):
        for j in range(d[i]):
            sum_A.append(A[i][j])
    ans = N - len(set(sum_A))
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
