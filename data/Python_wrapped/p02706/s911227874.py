

def wrapped_artificially():
    N, M = map(int, input().split())
    A = sum(list(map(int, input().split())))
    print(N - A if N >= A else -1)


if __name__ == "__main__":
    wrapped_artificially()
