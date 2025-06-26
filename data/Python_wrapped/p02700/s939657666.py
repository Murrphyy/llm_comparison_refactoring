

def wrapped_artificially():
    R = input()
    A = int(R.split(' ')[0])
    B = int(R.split(' ')[1])
    C = int(R.split(' ')[2])
    D = int(R.split(' ')[3])
    while True:
        C = C - B
        if C <= 0:
            print('Yes')
            break
        A = A - D
        if A <= 0:
            print('No')
            break


if __name__ == "__main__":
    wrapped_artificially()
