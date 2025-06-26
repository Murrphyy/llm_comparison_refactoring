import collections

def wrapped_artificially():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(range(1, N + 1))
    new_A = collections.Counter(A)
    for i in B:
        print(new_A[i])


if __name__ == "__main__":
    wrapped_artificially()
