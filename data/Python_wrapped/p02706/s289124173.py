

def wrapped_artificially():
    n, m = map(int, input().split())
    *a, = map(int, input().split())
    ans = n - sum(a)
    print([-1, ans][ans >= 0])


if __name__ == "__main__":
    wrapped_artificially()
