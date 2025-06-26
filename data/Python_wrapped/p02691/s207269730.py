import collections

def wrapped_artificially():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    tempi = [0] * n
    tempj = [0] * n
    for i in range(n):
        tempi[i] = a[i] + i + 1
    for i in range(n):
        tempj[i] = -a[i] + i + 1
    tempid = collections.Counter(tempi)
    tempjd = collections.Counter(tempj)
    for k in tempid.keys():
        a = tempid[k]
        b = tempjd[k]
        ans = ans + a * b
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
