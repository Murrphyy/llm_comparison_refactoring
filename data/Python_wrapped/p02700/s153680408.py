

def wrapped_artificially():
    A, B, C, D = map(int, input().split())
    while A >= 0 or C >= 0:
        C = C - B
        if C <= 0:
            print('Yes')
            exit()
        A = A - D
        if A <= 0:
            print('No')
            exit()


if __name__ == "__main__":
    wrapped_artificially()
