def getInts():
    return [int(x) for x in input().split()]

def wrapped_artificially():
    [N] = getInts()
    As = getInts()
    A = {}
    for i in range(1, N + 1):
        A[i] = As[i - 1]
    L = {}
    R = {}
    for i in range(1, N + 1):
        if i - A[i] not in L:
            L[i - A[i]] = 1
        else:
            L[i - A[i]] += 1
        if i + A[i] not in R:
            R[i + A[i]] = 1
        else:
            R[i + A[i]] += 1
    count = 0
    for k in R.keys():
        if k in L:
            count += R[k] * L[k]
    print(count)


if __name__ == "__main__":
    wrapped_artificially()
