

def wrapped_artificially():
    N, K = map(int, input().split())
    have = [False] * N
    for _ in range(K):
        d = int(input())
        a = list(map(int, input().split()))
        for i in a:
            have[i - 1] = True
    ans = have.count(False)
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
