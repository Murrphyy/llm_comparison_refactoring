

def wrapped_artificially():
    n, m = [int(x) for x in input().split()]
    h = [int(x) for x in input().split()]
    t = [[] for i in range(n)]
    ans = 0
    for i in range(m):
        a, b = [int(x) for x in input().split()]
        t[a - 1].append(b - 1)
        t[b - 1].append(a - 1)
    for i in range(n):
        if t[i] == []:
            ans += 1
        else:
            c = []
            for j in t[i]:
                if h[i] <= h[j]:
                    c.append(False)
            if c == []:
                ans += 1
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
