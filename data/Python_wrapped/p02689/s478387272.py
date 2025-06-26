

def wrapped_artificially():
    n, m = map(int, input().split())
    height = [int(i) for i in input().split()]
    neighbors = {}
    for _ in range(m):
        a, b = map(int, input().split())
        if a not in neighbors:
            neighbors.update({a: set()})
        if b not in neighbors[a]:
            neighbors[a].add(b)
        if b not in neighbors:
            neighbors.update({b: set()})
        if a not in neighbors[b]:
            neighbors[b].add(a)
    count = 0
    visited = set()
    for std, s in neighbors.items():
        flag = True
        visited.add(std)
        height_std = height[std - 1]
        for each in s:
            h = height[each - 1]
            if height_std <= h:
                flag = False
                break
        if flag:
            count += 1
    for i in range(n):
        if i + 1 not in visited:
            count += 1
    print(count)


if __name__ == "__main__":
    wrapped_artificially()
