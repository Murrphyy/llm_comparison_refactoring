

def wrapped_artificially():
    A, B, C, D = map(int, input().split())
    while True:
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
