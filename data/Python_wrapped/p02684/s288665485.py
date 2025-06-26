

def wrapped_artificially():
    N, K = map(int, input().split())
    tele = list(map(int, input().split()))
    now = 0
    goal, loop, visit = ([], [], [0] * N)
    while visit[now] != 2:
        if visit[now] == 0:
            goal.append(now)
        else:
            loop.append(now)
        visit[now] += 1
        now = tele[now] - 1
    if len(goal) > K:
        print(goal[K] + 1)
    else:
        res = len(goal) - len(loop)
        print(loop[(K - res) % len(loop)] + 1)


if __name__ == "__main__":
    wrapped_artificially()
