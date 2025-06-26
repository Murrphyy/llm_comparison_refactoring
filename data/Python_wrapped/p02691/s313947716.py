import collections

def wrapped_artificially():
    N = int(input())
    A = list(map(int, input().split()))
    i = [k for k in range(1, N + 1)]
    j = [k for k in range(1, N + 1)]
    Li = [i[k] + A[k] for k in range(N)]
    Rj = [j[k] - A[k] for k in range(N)]
    Li = collections.Counter(Li)
    counter = 0
    for r in Rj:
        counter += Li[r]
    print(counter)


if __name__ == "__main__":
    wrapped_artificially()
