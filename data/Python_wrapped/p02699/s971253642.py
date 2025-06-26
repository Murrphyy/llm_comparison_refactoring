import sys
def solve(S: int, W: int):
    print('unsafe' if W >= S else 'safe')
    return
def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = int(next(tokens))
    W = int(next(tokens))
    solve(S, W)

def wrapped_artificially():
    sys.setrecursionlimit(10 ** 9)
    INF = 10 ** 20
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
