import itertools

def wrapped_artificially():
    n, m, q = map(int, input().split())
    abcd = []
    for _ in range(q):
        abcd.append(list(map(int, input().split())))
    ans = 0
    for l in itertools.combinations_with_replacement(range(1, m + 1), n):
        tmp = 0
        for i in range(q):
            a, b, c, d = abcd[i]
            if l[b - 1] - l[a - 1] == c:
                tmp += d
        ans = max(ans, tmp)
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
