

def wrapped_artificially():
    N, M = map(int, input().split())
    A = [int(x) for x in input().split()]
    sm = sum(A)
    print(N - sm if N >= sm else -1)


if __name__ == "__main__":
    wrapped_artificially()
