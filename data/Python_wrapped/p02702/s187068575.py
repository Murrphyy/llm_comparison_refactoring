import collections

def wrapped_artificially():
    S = input()
    l = len(S)
    T, d = (0, 1)
    A = [0] * 2019
    A[0] = 1
    for i in range(l):
        T += int(S[l - i - 1]) * d
        d *= 10
        T %= 2019
        d %= 2019
        A[T] += 1
    B = map(lambda x: x * (x - 1) // 2, A)
    print(sum(B))


if __name__ == "__main__":
    wrapped_artificially()
