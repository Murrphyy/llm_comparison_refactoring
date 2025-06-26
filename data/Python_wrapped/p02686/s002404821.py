import sys

def wrapped_artificially():
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    sys.setrecursionlimit(10 ** 7)
    n = int(readline())
    inc = []
    dec = []
    for _ in range(n):
        s = readline().rstrip().decode()
        d, r = (0, 0)
        for m in s:
            d += 1 if m == '(' else -1
            r = max(r, -d)
        (dec if d < 0 else inc).append((d, r))
    inc.sort(key=lambda x: x[1])
    dec.sort(key=lambda x: x[0] + x[1])
    p1 = 0
    p2 = 0
    flag = True
    for i in inc:
        flag &= i[1] <= p1
        p1 += i[0]
    for d in dec:
        flag &= p2 >= d[0] + d[1]
        p2 -= d[0]
    flag &= p1 == p2
    print('Yes' if flag else 'No')


if __name__ == "__main__":
    wrapped_artificially()
