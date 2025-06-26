def resolve():
    A, B, C, D = list(map(int, input().split()))
    while True:
        C -= B
        if C <= 0:
            print('Yes')
            break
        A -= D
        if A <= 0:
            print('No')
            break
    return

def wrapped_artificially():
    resolve()


if __name__ == "__main__":
    wrapped_artificially()
