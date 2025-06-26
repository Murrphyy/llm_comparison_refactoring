import sys, queue, math, copy, itertools, bisect, collections, heapq
def main():
    sys.setrecursionlimit(10 ** 7)
    INF = 10 ** 7
    LI = lambda: [int(x) for x in sys.stdin.readline().split()]
    NI = lambda: int(sys.stdin.readline())
    N = NI()
    up = 0
    down = 0
    mp = []
    mm = []
    for _ in range(N):
        w = INF
        e = 0
        for s in sys.stdin.readline().rstrip():
            if s == '(':
                e += 1
            else:
                e -= 1
            w = min(w, e)
        if w < 0:
            if e > 0:
                mp.append((w, e))
            elif w == e:
                down += e
            else:
                mm.append((w, e))
        else:
            up += e
    mp.sort(reverse=True)
    for w, e in mp:
        if up + w < 0:
            print('No')
            exit(0)
        up += e
    mm.sort(reverse=True)
    for w, e in mm:
        if down - w > 0:
            print('No')
            exit(0)
        down += e
    if up + down == 0:
        print('Yes')
    else:
        print('No')

def wrapped_artificially():
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
