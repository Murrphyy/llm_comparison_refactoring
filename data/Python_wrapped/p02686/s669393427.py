import sys
from collections import deque
import heapq
from itertools import combinations
import bisect

def wrapped_artificially():
    sys.setrecursionlimit(10 ** 9)
    n = int(input())
    l = []
    for i in range(n):
        l.append(list(input()))
    p = 0
    q = 0
    for i in range(n):
        for j in l[i]:
            if j == '(':
                p += 1
            else:
                q += 1
    if p != q:
        print('No')
        exit()
    pl = []
    ql = []
    ml = []
    for i in range(n):
        a = l[i]
        p = 0
        q = 0
        for j in a:
            if j == '(':
                p += 1
            else:
                q += 1
        if p > q:
            pl.append(a)
        elif p < q:
            ql.append(a)
        else:
            ml.append(a)
    if pl:
        pp = []
        for i in pl:
            d = 0
            t = 0
            for j in i:
                if j == '(':
                    d += 1
                else:
                    d -= 1
                t = max(t, -d)
            pp.append([t, d])
        pp.sort(key=lambda x: x[0] * 10 ** 6 - x[1])
        dd = 0
        for a, b in pp:
            if dd < a:
                print('No')
                exit()
            dd += b
    if ml:
        pp = []
        for i in ml:
            d = 0
            t = 0
            for j in i:
                if j == '(':
                    d += 1
                else:
                    d -= 1
                t = max(t, -d)
            pp.append([t, d])
        if not pl:
            dd = 0
        for a, b in pp:
            if dd < a:
                print('No')
                exit()
            dd += b
    if ql:
        pp = []
        for i in ql:
            d = 0
            t = 0
            for j in range(len(i)):
                if i[len(i) - 1 - j] == ')':
                    d += 1
                else:
                    d -= 1
                t = max(t, -d)
            pp.append([t, d])
        pp.sort(key=lambda x: x[0] * 10 ** 6 - x[1])
        dd = 0
        for a, b in pp:
            if dd < a:
                print('No')
                exit()
            dd += b
    if ml:
        pp = []
        for i in ml:
            d = 0
            t = 0
            for j in range(len(i)):
                if i[len(i) - 1 - j] == ')':
                    d += 1
                else:
                    d -= 1
                t = max(t, -d)
            pp.append([t, d])
        if not ql:
            dd = 0
        for a, b in pp:
            if dd < a:
                print('No')
                exit()
            dd += b
    print('Yes')


if __name__ == "__main__":
    wrapped_artificially()
