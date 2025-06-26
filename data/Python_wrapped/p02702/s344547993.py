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
    S = list(map(int, LS()))
    S = S[::-1]
    ln = len(S)
    mod = 2019
    times = 1
    for i in range(ln):
        S[i] = S[i] * times
        times = times * 10 % mod
    R = [0] * (ln + 1)
    memo = {0: 1}
    ans = 0
    for i in range(1, ln + 1):
        tmp = (R[i - 1] + S[i - 1]) % mod
        R[i] = tmp
        cnt = memo.get(tmp, 0)
        ans = ans + cnt
        memo[tmp] = cnt + 1
    print(ans)

def wrapped_artificially():
    sys.setrecursionlimit(10 ** 9)
    INF = float('inf')
    if __name__ == '__main__':
        solve()


if __name__ == "__main__":
    wrapped_artificially()
