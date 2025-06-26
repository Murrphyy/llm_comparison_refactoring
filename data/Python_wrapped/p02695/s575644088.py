from itertools import *

def wrapped_artificially():
    N, M, Q = map(int, input().split())
    abcd = [list(map(int, input().split())) for q in range(Q)]
    print(max((sum((d for a, b, c, d in abcd if i[b - 1] - i[a - 1] == c)) for i in combinations_with_replacement(range(M), N))))


if __name__ == "__main__":
    wrapped_artificially()
