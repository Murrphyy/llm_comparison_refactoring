

def wrapped_artificially():
    n, k = map(int, input().split())
    t = [0] * n
    for _ in range(k):
        d = int(input())
        a = list(map(int, input().split()))
        for e in a:
            t[e - 1] += 1
    ans = 0
    l = [i for i in t if i == 0]
    print(len(l))


if __name__ == "__main__":
    wrapped_artificially()
