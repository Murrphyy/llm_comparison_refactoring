

def wrapped_artificially():
    n, k = map(int, input().split())
    x = [0] * n
    for i in range(k):
        z = int(input())
        if z == 1:
            x[int(input()) - 1] += 1
        else:
            a = list(map(int, input().split()))
            for j in a:
                x[j - 1] += 1
    print(x.count(0))


if __name__ == "__main__":
    wrapped_artificially()
