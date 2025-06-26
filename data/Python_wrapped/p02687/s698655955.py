def inN():
    return int(input())
def inL():
    return list(map(int, input().split()))
def inNL(n):
    return [list(map(int, input().split())) for i in range(n)]

def wrapped_artificially():
    mod = pow(10, 9) + 7
    s = input()
    if s == 'ABC':
        print('ARC')
    else:
        print('ABC')


if __name__ == "__main__":
    wrapped_artificially()
