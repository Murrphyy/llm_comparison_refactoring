import numpy as np

def wrapped_artificially():
    N, M = map(int, input().split())
    h = np.array(list(map(int, input().split())))
    x = dict()
    for _ in range(M):
        a, b = map(int, input().split())
        if a - 1 not in x.keys():
            x[a - 1] = []
        if b - 1 not in x.keys():
            x[b - 1] = []
        x[a - 1].append(b - 1)
        x[b - 1].append(a - 1)
    ans = 0
    for k, v in x.items():
        cand = h[k]
        tied = h[np.array(v)]
        ans += [0, 1][sum(tied >= cand) == 0]
    ans += N - len(x.keys())
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
