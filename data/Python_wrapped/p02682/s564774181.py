import sys

def wrapped_artificially():
    A, B, C, K = map(int, input().split())
    if not (0 <= A and 0 <= B and (0 <= C)):
        sys.exit()
    if not (1 <= K <= A + B + C and A + B + C <= 2 * 10 ** 9):
        sys.exit()
    sum = 0
    if A >= 1 and K <= A:
        print(K)
        sys.exit()
    elif A >= 1 and K > A:
        sum += A
        K -= A
        A = 0
    if B >= 1 and K <= B:
        print(sum)
        sys.exit()
    elif B >= 1 and K > B:
        K -= B
        B = 0
    if C >= 1 and K <= C:
        sum -= K
        C = 0
    elif C >= 1 and K > C:
        sum -= C
        print(sum)
        sys.exit()
    print(sum)


if __name__ == "__main__":
    wrapped_artificially()
