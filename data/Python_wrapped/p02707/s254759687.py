from collections import defaultdict

def wrapped_artificially():
    n = int(input())
    a = [int(i) for i in input().split()]
    mapping = defaultdict(int)
    for _a, i in zip(range(2, n + 1), a):
        mapping[i] += 1
    for i in range(1, n + 1):
        print(mapping[i])


if __name__ == "__main__":
    wrapped_artificially()
