

def wrapped_artificially():
    N, K = map(int, input().split())
    A = [0] + list(map(int, input().split()))
    now = 1
    visited = []
    visited_set = set()
    flag = False
    for i in range(1, K + 1):
        visited.append(now)
        visited_set.add(now)
        now = A[now]
        if now in visited_set:
            loop_start = visited.index(now)
            loop_length = i - loop_start
            flag = True
            break
    else:
        print(now)
    if flag:
        print(visited[loop_start + (K - loop_start) % loop_length])


if __name__ == "__main__":
    wrapped_artificially()
