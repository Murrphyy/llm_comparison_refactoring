from itertools import combinations_with_replacement as combi

def wrapped_artificially():
    N, M, Q = map(int, input().split())
    a = [0] * Q
    b = [0] * Q
    c = [0] * Q
    d = [0] * Q
    l = [i + 1 for i in range(M)]
    point = 0
    for i in range(Q):
        a[i], b[i], c[i], d[i] = map(int, input().split())
    for v in combi(l, N):
        tmp = 0
        for j in range(Q):
            if v[b[j] - 1] - v[a[j] - 1] == c[j]:
                tmp += d[j]
        point = max(point, tmp)
    print(point)


if __name__ == "__main__":
    wrapped_artificially()
