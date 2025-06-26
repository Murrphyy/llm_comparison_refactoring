from sys import stdin
def main():
    N, M = list(map(int, input().split()))
    H = list(map(int, input().split()))
    G = [[] for _ in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)
    cnt = 0
    for i in range(N):
        for j in G[i]:
            if H[i] <= H[j]:
                break
        else:
            cnt += 1
    print(cnt)

def wrapped_artificially():
    input = stdin.readline
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
