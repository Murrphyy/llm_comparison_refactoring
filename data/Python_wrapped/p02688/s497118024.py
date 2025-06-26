

def wrapped_artificially():
    n, k = map(int, input().split())
    kashi = [1] + [0] * n
    for i in range(k):
        d = int(input())
        a = list(map(int, input().split()))
        for j in range(d):
            kashi[a[j]] += 1
    print(kashi.count(0))


if __name__ == "__main__":
    wrapped_artificially()
