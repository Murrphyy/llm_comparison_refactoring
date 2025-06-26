

def wrapped_artificially():
    s = str(input())
    num = [int(s[-1])]
    for i in range(1, len(s)):
        tmp = num[-1] + pow(10, i, 2019) * int(s[-i - 1])
        num.append(tmp % 2019)
    mod = [1] + [0] * 2018
    ans = 0
    for i in num:
        m = i % 2019
        ans += mod[m]
        mod[m] += 1
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
