import sys

def wrapped_artificially():
    n = int(input())
    si = []
    for _ in range(n):
        s = input()
        l = 0
        r = 0
        count = 0
        for i in range(len(s)):
            if s[i] == '(':
                count += 1
            else:
                count = max(0, count - 1)
        l = count
        count = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ')':
                count += 1
            else:
                count = max(0, count - 1)
        r = count
        si.append((l, r))
    if len(si) == 1:
        if si[0] == (0, 0):
            print('Yes')
            sys.exit()
    index_l = -1
    index_r = -1
    maxi_l = 0
    maxi_r = 0
    for i in range(n):
        a, b = si[i]
        if a == 0:
            if maxi_l < b:
                maxi_l = b
                index_l = i
        if b == 0:
            if maxi_r < a:
                maxi_r = a
                index_r = i
    count = 0
    if index_r < index_l:
        count += si.pop(index_l)[1]
        last = si.pop(index_r)
    else:
        last = si.pop(index_r)
        count += si.pop(index_l)[1]
    minus = []
    plus = []
    while si:
        a, b = si.pop()
        if a <= b:
            plus.append((a, b))
        else:
            minus.append((a, b))
    plus.sort()
    minus.sort(reverse=True, key=lambda x: x[1])
    for a, b in plus:
        if count >= a:
            count += b - a
        else:
            print('No')
            sys.exit()
    for a, b in minus:
        if count >= a:
            count += b - a
        else:
            print('No')
            sys.exit()
    count -= last[0]
    if count == 0:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    wrapped_artificially()
