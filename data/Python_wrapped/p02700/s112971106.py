

def wrapped_artificially():
    A, B, C, D = map(int, input().split())
    while A > 0 and C > 0:
        C -= B
        A -= D
        if C <= 0:
            print('Yes')
            break
        elif A <= 0:
            print('No')


if __name__ == "__main__":
    wrapped_artificially()
