import sys

def wrapped_artificially():
    input = sys.stdin.readline
    n = int(input())
    cnt = []
    for i in range(n):
        s = input().rstrip()
        l = s.count('(')
        r = s.count(')')
        minus = 0
        now = 0
        for j in range(len(s)):
            if s[j] == '(':
                now += 1
            else:
                now -= 1
                minus = min(minus, now)
        cnt.append((l, r, s, minus))
    cnt.sort(key=lambda x: x[1] - x[0])
    plus = []
    minus = []
    first = []
    for x in cnt:
        if x[3] >= 0:
            first.append(x)
        elif x[0] - x[1] > 0:
            plus.append(x)
        else:
            minus.append(x)
    plus.sort(key=lambda x: -x[3])
    minus.sort(key=lambda x: -(x[0] - x[1] - x[3]))
    l = r = 0
    for x in first + plus + minus:
        for i in range(len(x[2])):
            if x[2][i] == '(':
                l += 1
            else:
                r += 1
            if l < r:
                print('No')
                exit()
    if l == r:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    wrapped_artificially()
