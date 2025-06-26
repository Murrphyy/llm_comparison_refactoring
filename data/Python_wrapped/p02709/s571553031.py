import numpy as np
import sys

def wrapped_artificially():
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    N = int(readline())
    A = np.array(read().split(), np.int64)
    I = np.argsort(A)[::-1].tolist()
    A = A[I].tolist()
    dp = np.zeros(1, np.int64)
    for n, (i, x) in enumerate(zip(I, A)):
        newdp = np.zeros(len(dp) + 1, np.int64)
        left_ind = np.arange(len(dp))
        right_ind = N - 1 - n + left_ind
        left_cost = x * np.abs(left_ind - i)
        right_cost = x * np.abs(right_ind - i)
        np.maximum(newdp[:-1], dp + right_cost, out=newdp[:-1])
        np.maximum(newdp[1:], dp + left_cost, out=newdp[1:])
        dp = newdp
    print(dp.max())


if __name__ == "__main__":
    wrapped_artificially()
