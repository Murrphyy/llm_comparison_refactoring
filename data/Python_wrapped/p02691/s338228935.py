import sys
def main():
    read = lambda: sys.stdin.readline().rstrip()
    import collections
    d = collections.defaultdict(int)
    N = int(read())
    A = list(map(int, read().split()))
    cnt = 0
    for i, x in enumerate(A):
        d[i + x] += 1
        if d[i - x] > 0:
            cnt += d[i - x]
    print(cnt)

def wrapped_artificially():
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
