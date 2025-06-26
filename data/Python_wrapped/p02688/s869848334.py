

def wrapped_artificially():
    n, k = map(int, input().split())
    sum = [0] * n
    for i in range(k):
        d = int(input())
        a = [int(s) for s in input().split()]
        for j in range(d):
            sum[a[j] - 1] += 1
    print(sum.count(0))


if __name__ == "__main__":
    wrapped_artificially()
