import sys

def wrapped_artificially():
    A, B, C, D = map(int, input().split())
    if not (1 <= A <= 100 and 1 <= B <= 100 and (1 <= C <= 100) and (1 <= D <= 100)):
        sys.exit()
    while A >= 1 and C >= 1:
        C -= B
        if C <= 0:
            print('Yes')
            break
        A -= D
        if A <= 0:
            print('No')
            break


if __name__ == "__main__":
    wrapped_artificially()
