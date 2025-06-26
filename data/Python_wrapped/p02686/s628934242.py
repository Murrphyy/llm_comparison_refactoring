import sys
def change(S):
    MIN = 0
    SUM = 0
    for i in S:
        if i == ')':
            SUM -= 1
            MIN = min(MIN, SUM)
        else:
            SUM += 1
    MIN *= -1
    return (MIN, SUM)

def wrapped_artificially():
    N = int(input())
    B1 = []
    B2 = []
    for _ in range(N):
        b = change(input())
        if b[1] > 0:
            B1.append(b)
        else:
            B2.append((b[0] + b[1], b[0], b[1]))
    B1.sort()
    B2.sort(reverse=True)
    cnt = 0
    for b in B1:
        if cnt < b[0]:
            print('No')
            sys.exit()
        cnt += b[1]
    for b in B2:
        if cnt < b[1]:
            print('No')
            sys.exit()
        cnt += b[2]
    if cnt == 0:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    wrapped_artificially()
