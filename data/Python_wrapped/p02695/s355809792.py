from itertools import combinations_with_replacement

def wrapped_artificially():
    N, M, Q = map(int, input().split())
    num = []
    for i in range(Q):
        num.append(list(map(int, input().split())))
    lst = list(combinations_with_replacement([i for i in range(1, M + 1)], N))
    ans = 0
    for q in lst:
        ans_tmp = 0
        for i in range(Q):
            if q[num[i][1] - 1] - q[num[i][0] - 1] == num[i][2]:
                ans_tmp += num[i][3]
        if ans < ans_tmp:
            ans = ans_tmp
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
