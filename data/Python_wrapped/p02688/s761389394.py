

def wrapped_artificially():
    N, K = map(int, input().split())
    d = 0
    A = []
    ans = 0
    for i in range(K):
        d = int(input())
        A.append(input().split())
    for i in range(1, N + 1):
        for j in range(len(A)):
            if str(i) in A[j]:
                break
            if j == len(A) - 1:
                ans += 1
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
