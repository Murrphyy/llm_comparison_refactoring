import sys
def dfs(a_l):
    if len(a_l) == n:
        global ans
        t_ans = 0
        for a, b, c, d in l:
            a -= 1
            b -= 1
            if a_l[b] - a_l[a] == c:
                t_ans += d
        ans = max(ans, t_ans)
        return
    a_last = a_l[-1]
    for i in range(a_last, m + 1):
        dfs(a_l + [i])

def wrapped_artificially():
    sys.setrecursionlimit(10 ** 9)
    n, m, q = map(int, input().split())
    l = [list(map(int, input().split())) for i in range(q)]
    ans = 0
    for i in range(1, m + 1):
        dfs([i])
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
