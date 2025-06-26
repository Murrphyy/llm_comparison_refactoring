import sys
def solve(A: int, B: int, N: int):
    if A == 1:
        return 0
    if N < B:
        x = N
    else:
        md = N % B
        x = int(N - (md + 1))
    return int(A * x // B) - A * int(x // B)
def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))
    B = int(next(tokens))
    N = int(next(tokens))
    print(solve(A, B, N))

def wrapped_artificially():
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
