

def wrapped_artificially():
    s = input()
    res = 0
    m = 1
    p = [0] * 2019
    for i in map(int, s[::-1]):
        res += i * m
        res %= 2019
        p[res] += 1
        m *= 10
        m %= 2019
    print(p[0] + sum([i * (i - 1) // 2 for i in p]))


if __name__ == "__main__":
    wrapped_artificially()
