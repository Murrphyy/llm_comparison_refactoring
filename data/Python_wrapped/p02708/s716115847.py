

def wrapped_artificially():
    n, k = map(int, input().split())
    res = 0
    divnum = 10 ** 9 + 7
    for i in range(k, n + 2):
        res += i * (n - i + 1) + 1
        res %= divnum
    print(res)


if __name__ == "__main__":
    wrapped_artificially()
