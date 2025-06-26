import sys
def solve(A: int, B: int, C: int, D: int):
    while True:
        C -= B
        if C <= 0:
            print(YES)
            break
        A -= D
        if A <= 0:
            print(NO)
            break
    return
def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))
    B = int(next(tokens))
    C = int(next(tokens))
    D = int(next(tokens))
    solve(A, B, C, D)

def wrapped_artificially():
    sys.setrecursionlimit(10 ** 9)
    YES = 'Yes'
    NO = 'No'
    INF = 10 ** 20
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
