

def wrapped_artificially():
    a, b, c, d = map(int, input().split())
    taka_cnt = c // b if c % b == 0 else c // b + 1
    aoki_cnt = a // d if a % d == 0 else a // d + 1
    print('Yes' if taka_cnt <= aoki_cnt else 'No')


if __name__ == "__main__":
    wrapped_artificially()
