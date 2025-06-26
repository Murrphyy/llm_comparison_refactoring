import collections
import bisect

def wrapped_artificially():
    n = int(input())
    cnt = collections.defaultdict(list)
    dat = list(map(int, input().split()))
    buf = []
    for i in range(n):
        cnt[i - dat[i]].append(i)
    res = 0
    for i in range(n):
        x = i + dat[i]
        if x in cnt:
            res += len(cnt[x]) - bisect.bisect_left(cnt[x], x)
    print(res)


if __name__ == "__main__":
    wrapped_artificially()
