import sys
import heapq

def wrapped_artificially():
    input = sys.stdin.readline
    N = int(input())
    forward = []
    backward = []
    for _ in range(N):
        pos = 0
        Min = 0
        for c in input()[:-1]:
            if c == '(':
                pos += 1
            else:
                pos -= 1
                Min = min(Min, pos)
        if pos >= 0:
            heapq.heappush(forward, (-Min, pos))
        else:
            heapq.heappush(backward, (pos - Min, -pos))
    ansflg = True
    pos1 = 0
    while forward:
        down, pos = heapq.heappop(forward)
        if pos1 >= down:
            pos1 += pos
        else:
            ansflg = False
            break
    pos2 = 0
    if ansflg:
        while backward:
            down, pos = heapq.heappop(backward)
            if pos2 >= down:
                pos2 += pos
            else:
                ansflg = False
                break
    if pos1 != pos2:
        ansflg = False
    if ansflg:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    wrapped_artificially()
