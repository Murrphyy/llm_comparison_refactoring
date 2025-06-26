import sys
import numpy as np

def wrapped_artificially():
    input = sys.stdin.readline
    sw = np.array([int(x) for x in input().split()])
    ans = 'unsafe' if sw[1] >= sw[0] else 'safe'
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
