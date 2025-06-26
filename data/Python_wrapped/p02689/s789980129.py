

def wrapped_artificially():
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    A = [[] for i in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        A[a - 1].append(h[b - 1])
        A[b - 1].append(h[a - 1])
    count = 0
    for i in range(n):
        if A[i] == []:
            count += 1
        elif max(A[i]) < h[i]:
            count += 1
        else:
            continue
    print(count)


if __name__ == "__main__":
    wrapped_artificially()
