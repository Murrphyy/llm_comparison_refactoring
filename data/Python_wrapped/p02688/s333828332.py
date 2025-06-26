

def wrapped_artificially():
    n, k = map(int, input().split())
    have = [False] * n
    for _ in range(k):
        d = int(input())
        A = list(map(int, input().split()))
        for a in A:
            have[a - 1] = True
    ans = 0
    for i in range(n):
        if have[i] == False:
            ans += 1
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
