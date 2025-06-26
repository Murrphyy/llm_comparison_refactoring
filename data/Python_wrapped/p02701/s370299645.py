

def wrapped_artificially():
    N = int(input())
    S = [str(input()) for _ in range(N)]
    S = set(S)
    print(len(S))


if __name__ == "__main__":
    wrapped_artificially()
