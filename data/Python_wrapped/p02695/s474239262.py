import itertools

def wrapped_artificially():
    N, M, Q = map(int, input().split())
    abcd = [list(map(int, input().split())) for i in range(Q)]
    ans = 0
    for A in itertools.combinations_with_replacement(range(1, M + 1), N):
        score = 0
        for i in range(Q):
            a = abcd[i][0]
            b = abcd[i][1]
            c = abcd[i][2]
            d = abcd[i][3]
            if A[b - 1] - A[a - 1] == c:
                score += d
        ans = max(ans, score)
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
