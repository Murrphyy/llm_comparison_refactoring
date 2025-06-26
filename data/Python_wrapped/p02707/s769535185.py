from collections import defaultdict

def wrapped_artificially():
    n = int(input())
    a = list(map(int, input().split()))
    d = defaultdict(int)
    for i in a:
        d[i] += 1
    for i in range(1, n + 1):
        print(d[i])


if __name__ == "__main__":
    wrapped_artificially()
