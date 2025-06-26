import sys
import math
from bisect import bisect_right as br
from bisect import bisect_left as bl
from heapq import heappush, heappop, heappushpop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter
from itertools import permutations
def I():
    return int(sys.stdin.readline())
def LI():
    return list(map(int, sys.stdin.readline().split()))

def wrapped_artificially():
    sys.setrecursionlimit(2147483647)
    mod = 10 ** 9 + 7
    inf = float('inf')
    n, k = LI()
    a = LI()
    check_num = [-1] * n
    idx = 0
    cnt = 1
    while 1:
        idx = a[idx] - 1
        if check_num[idx] != -1:
            s = check_num[idx] - 1
            cnt -= 1
            break
        check_num[idx] = cnt
        cnt += 1
    if cnt >= k:
        for i in range(n):
            if check_num[i] == k:
                print(i + 1)
                quit()
    else:
        roop_num = cnt - s
        x = (k - (s + 1)) % roop_num
        for i in range(n):
            if check_num[i] - s - 1 == x:
                print(i + 1)
                quit()


if __name__ == "__main__":
    wrapped_artificially()
