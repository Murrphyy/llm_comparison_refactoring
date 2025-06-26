

def wrapped_artificially():
    A, B, C, D = map(int, input().split())
    while A > 0 and C > 0:
        A -= D
        C -= B
    if C <= 0:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    wrapped_artificially()
