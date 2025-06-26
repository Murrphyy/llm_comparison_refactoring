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
    s, w = LI()
    if w >= s:
        print('unsafe')
    else:
        print('safe')


if __name__ == "__main__":
    wrapped_artificially()
