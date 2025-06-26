from collections import defaultdict

def wrapped_artificially():
    n = int(input())
    a = list(map(int, input().split()))
    d = defaultdict(int)
    sm = 0
    for i in range(n):
        d[i + a[i]] += 1
        sm += d[i - a[i]]
    print(sm)


if __name__ == "__main__":
    wrapped_artificially()
