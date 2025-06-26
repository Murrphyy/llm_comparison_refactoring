import itertools

def wrapped_artificially():
    n, m, q = map(int, input().split())
    a_list = []
    b_list = []
    c_list = []
    d_list = []
    for _ in range(q):
        a, b, c, d = map(int, input().split())
        a_list.append(a)
        b_list.append(b)
        c_list.append(c)
        d_list.append(d)
    ans = 0
    h_list = [i + 1 for i in range(m)]
    for A in itertools.combinations_with_replacement(h_list, n):
        max_d = 0
        for a, b, c, d in zip(a_list, b_list, c_list, d_list):
            if A[b - 1] - A[a - 1] == c:
                max_d += d
        ans = max(ans, max_d)
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
