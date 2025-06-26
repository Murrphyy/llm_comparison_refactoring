

def wrapped_artificially():
    n, k = map(int, input().split())
    b = list(range(1, n + 1))
    a = []
    for i in range(k):
        d = int(input())
        a += list(map(int, input().split()))
    a = list(set(a))
    num = 0
    for h in b:
        if h not in a:
            num += 1
    print(num)


if __name__ == "__main__":
    wrapped_artificially()
