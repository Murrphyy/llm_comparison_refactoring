

def wrapped_artificially():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    day = sum(a)
    if n >= day:
        print(n - day)
    else:
        print('-1')


if __name__ == "__main__":
    wrapped_artificially()
