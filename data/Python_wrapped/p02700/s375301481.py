def N():
    return int(input())
def L():
    return list(map(int, input().split()))
def NL(n):
    return [list(map(int, input().split())) for i in range(n)]

def wrapped_artificially():
    mod = pow(10, 9) + 7
    a, b, c, d = L()
    ta = -(-c // b)
    ao = -(-a // d)
    if ta <= ao:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    wrapped_artificially()
