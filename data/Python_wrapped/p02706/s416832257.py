import sys
def int1(x):
    return int(x) - 1
def II():
    return int(input())
def MI():
    return map(int, input().split())
def MI1():
    return map(int1, input().split())
def LI():
    return list(map(int, input().split()))
def LI1():
    return list(map(int1, input().split()))
def LLI(rows_number):
    return [LI() for _ in range(rows_number)]
def MS():
    return input().split()
def LS():
    return list(input())
def LLS(rows_number):
    return [LS() for _ in range(rows_number)]
def printlist(lst, k=' '):
    print(k.join(list(map(str, lst))))
def solve():
    N, M = MI()
    A = LI()
    ans = N - sum(A)
    print(-1 if ans < 0 else ans)

def wrapped_artificially():
    sys.setrecursionlimit(10 ** 9)
    INF = float('inf')
    if __name__ == '__main__':
        solve()


if __name__ == "__main__":
    wrapped_artificially()
