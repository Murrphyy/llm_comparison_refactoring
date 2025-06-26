

def wrapped_artificially():
    n, k = map(int, input().split())
    treat = [1] * n
    for i in range(k):
        d = int(input())
        c = list(map(int, input().split()))
        for j in c:
            treat[j - 1] = 0
    print(sum(treat))


if __name__ == "__main__":
    wrapped_artificially()
