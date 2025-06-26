

def wrapped_artificially():
    N, K = map(int, input().split())
    l = [False for x in range(N)]
    for i in range(K):
        d = int(input())
        A = list(map(int, input().split()))
        for j in A:
            l[j - 1] = True
    print(l.count(False))


if __name__ == "__main__":
    wrapped_artificially()
