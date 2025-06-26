import sys
def main():
    N = int(sys.stdin.readline())
    A = tuple(map(int, sys.stdin.readline().split()))
    R = [0 for _ in range(N)]
    for a in A:
        R[a - 1] += 1
    for r in R:
        print(r)

def wrapped_artificially():
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
