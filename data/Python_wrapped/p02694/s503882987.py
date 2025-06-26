import sys

def wrapped_artificially():
    input = sys.stdin.readline
    ins = lambda: input().rstrip()
    ini = lambda: int(input().rstrip())
    inm = lambda: map(int, input().split())
    inl = lambda: list(map(int, input().split()))
    n = ini()
    ans = 0
    count = 100
    while count < n:
        count += count // 100
        ans += 1
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
