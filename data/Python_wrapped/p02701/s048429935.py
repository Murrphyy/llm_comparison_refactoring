import numpy as np

def wrapped_artificially():
    if __name__ == '__main__':
        N = input()
        N = int(N)
        l = []
        for i in range(N):
            buf = input()
            l += [buf]
        l = np.array(l)
        print(len(np.unique(l)))


if __name__ == "__main__":
    wrapped_artificially()
