import itertools

def wrapped_artificially():
    N, M, Q = map(int, input().split())
    List = []
    for i in range(Q):
        List.append(list(map(int, input().split())))
    List1 = []
    res = 0
    mid = 0
    for i in range(M):
        List1.append(i)
    x = itertools.combinations_with_replacement(List1, N)
    tryList = list(x)
    for tryElement in tryList:
        mid = 0
        for j in range(Q):
            if tryElement[List[j][1] - 1] - tryElement[List[j][0] - 1] == List[j][2]:
                mid += List[j][3]
        res = max(mid, res)
    print(res)


if __name__ == "__main__":
    wrapped_artificially()
