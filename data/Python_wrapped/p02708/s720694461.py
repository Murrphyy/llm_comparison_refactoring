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
def main():
    n, k = MI()
    m = 10 ** 9 + 7
    ans = 0
    for i in range(n - k + 2):
        ans += n * (n + 1) // 2 - i * (i - 1) // 2 - (n - i) * (n - i + 1) // 2 + 1
        ans %= m
    print(ans)

def wrapped_artificially():
    input = sys.stdin.buffer.readline
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
