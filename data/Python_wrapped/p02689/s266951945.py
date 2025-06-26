

def wrapped_artificially():
    n, m = map(int, input().split())
    hlist = list(map(int, input().split()))
    num = [0] * n
    for j in range(m):
        a, b = map(int, input().split())
        if hlist[a - 1] > hlist[b - 1]:
            num[b - 1] = 1
        elif hlist[a - 1] < hlist[b - 1]:
            num[a - 1] = 1
        elif hlist[a - 1] == hlist[b - 1]:
            num[a - 1] = 1
            num[b - 1] = 1
    print(num.count(0))


if __name__ == "__main__":
    wrapped_artificially()
