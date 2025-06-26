

def wrapped_artificially():
    N = int(input())
    A = list(map(int, input().split()))
    dic1 = {}
    dic2 = {}
    sum = 0
    for i in range(N):
        v = i - A[i]
        if v < 0:
            continue
        if not v in dic1:
            dic1[v] = 0
        dic1[v] += 1
    for i in range(N):
        v = i + A[i]
        if not v in dic2:
            dic2[v] = 0
        dic2[v] += 1
    for k, v in dic1.items():
        if not k in dic2:
            continue
        sum += dic1[k] * dic2[k]
    print(sum)


if __name__ == "__main__":
    wrapped_artificially()
