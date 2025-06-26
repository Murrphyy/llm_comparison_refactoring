from operator import itemgetter

def wrapped_artificially():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    A = []
    B = []
    for i in range(M):
        A0, B0 = map(int, input().split())
        A.append(A0)
        B.append(B0)
    C = [[i] for i in range(N)]
    HC = [[H[i]] for i in range(N)]
    for i in range(M):
        C[A[i] - 1].append(B[i] - 1)
        C[B[i] - 1].append(A[i] - 1)
        HC[A[i] - 1].append(H[B[i] - 1])
        HC[B[i] - 1].append(H[A[i] - 1])
    cnt = 0
    for i in range(N):
        C0 = []
        HC0 = []
        for cc, hcc in sorted(zip(C[i], HC[i]), key=itemgetter(1)):
            C0.append(cc)
            HC0.append(hcc)
        C[i] = C0
        HC[i] = HC0
        if C[i][-1] == i:
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    wrapped_artificially()
