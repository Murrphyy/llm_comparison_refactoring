import sys
def RD():
    return sys.stdin.read()
def II():
    return int(input())
def MI():
    return map(int, input().split())
def MF():
    return map(float, input().split())
def LI():
    return list(map(int, input().split()))
def LF():
    return list(map(float, input().split()))
def TI():
    return tuple(map(int, input().split()))
import numpy as np
def main():
    n, m = MI()
    H = LI()
    G = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = MI()
        G[a].append(H[b - 1])
        G[b].append(H[a - 1])
    ans = 0
    for i in range(1, n + 1):
        if G[i] == []:
            ans += 1
        elif H[i - 1] > max(G[i]):
            ans += 1
    print(ans)

def wrapped_artificially():
    input = sys.stdin.buffer.readline
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
