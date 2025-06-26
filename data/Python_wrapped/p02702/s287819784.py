

def wrapped_artificially():
    s = input()
    dic = {}
    cur = 0
    power = 0
    for i in range(0, len(s) + 1):
        s_int = len(s) - i - 1
        if cur in dic:
            dic[cur] += 1
        else:
            dic[cur] = 1
        try:
            num = int(s[s_int])
            cur += num * pow(10, power, 2019)
            cur %= 2019
            power += 1
        except IndexError:
            break
    res = 0
    for i in range(len(dic)):
        t = dic.popitem()
        cc = t[1]
        res += cc * (cc - 1) // 2
    print(res)


if __name__ == "__main__":
    wrapped_artificially()
