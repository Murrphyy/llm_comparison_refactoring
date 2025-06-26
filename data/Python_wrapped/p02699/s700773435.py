import sys
def solve(S: int, W: int):
    return 'unsafe' if W >= S else 'safe'
def main():
    sys.setrecursionlimit(10 ** 6)

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = int(next(tokens))
    W = int(next(tokens))
    print(solve(S, W))

def wrapped_artificially():
    INF = 1145141919
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
