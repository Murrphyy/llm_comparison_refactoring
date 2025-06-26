import numpy as np

def wrapped_artificially():
    n, k = map(int, input().split())
    a = np.arange(n + 1, dtype='int')
    b = np.cumsum(a)
    s = 0
    for i in range(k, n + 1):
        s += b[n] - b[n - i] - b[i - 1] + 1
        s = s % 1000000007
    s += 1
    s = s % 1000000007
    print(s)


if __name__ == "__main__":
    wrapped_artificially()
