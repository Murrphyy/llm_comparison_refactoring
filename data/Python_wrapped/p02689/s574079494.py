import sys

def wrapped_artificially():
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    N, M = map(int, readline().split())
    H = [0] + list(map(int, readline().split()))
    data = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, readline().split())
        data[a].append(b)
        data[b].append(a)
    flag = [True] * (N + 1)
    for i in range(1, N + 1):
        if flag[i] == False:
            continue
        for k in data[i]:
            if H[i] > H[k]:
                flag[k] = False
            else:
                flag[i] = False
    print(flag.count(True) - 1)


if __name__ == "__main__":
    wrapped_artificially()
