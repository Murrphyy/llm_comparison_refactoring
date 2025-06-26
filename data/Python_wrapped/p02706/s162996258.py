

def wrapped_artificially():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    print(max(-1, n - sum(a)))


if __name__ == "__main__":
    wrapped_artificially()
