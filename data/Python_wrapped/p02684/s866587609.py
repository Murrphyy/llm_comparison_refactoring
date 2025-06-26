

def wrapped_artificially():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    now = 0
    visited = set()
    visited.add(0)
    visited2 = [0]
    while True:
        k -= 1
        now = a[now] - 1
        if k == 0:
            print(now + 1)
            exit()
        if now in visited:
            visited.add(now)
            visited2.append(now)
            break
        visited.add(now)
        visited2.append(now)
    xxx = visited2[-1]
    cnt = []
    for i in range(len(visited2)):
        if visited2[i] == xxx:
            cnt.append(i)
    k %= cnt[1] - cnt[0]
    if k != 0:
        for i in range(k):
            now = a[now] - 1
    print(now + 1)


if __name__ == "__main__":
    wrapped_artificially()
