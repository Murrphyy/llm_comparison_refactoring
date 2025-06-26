import sys
def main():
    N, M = map(int, input().split())
    L = list(map(int, input().split()))
    i = 1
    R = list()
    p = set()
    for j in range(N + 1):
        if j == M - 1:
            print(L[i - 1])
            exit()
        if L[i - 1] in p:
            c = R.index(L[i - 1])
            t = len(R) - c
            m = R[c:]
            break
        R.append(L[i - 1])
        p.add(L[i - 1])
        i = L[i - 1]
    l = (M - c - 1) % t
    print(m[l])

def wrapped_artificially():
    input = sys.stdin.readline
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
