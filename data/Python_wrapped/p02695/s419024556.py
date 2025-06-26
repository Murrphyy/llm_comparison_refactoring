import sys
def rec(itr, lst):
    if itr == N:
        res = 0
        for a, b, c, d in abcd:
            if A[b - 1] - A[a - 1] == c:
                res += d
        return res
    else:
        res = 0
        for i in range(lst, M):
            A.append(i)
            res = max(res, rec(itr + 1, i))
            A.pop()
        return res

def wrapped_artificially():
    sys.setrecursionlimit(10 ** 6)
    N, M, Q = map(int, input().split())
    abcd = [list(map(int, input().split())) for i in range(Q)]
    A = []
    print(rec(0, 0))


if __name__ == "__main__":
    wrapped_artificially()
