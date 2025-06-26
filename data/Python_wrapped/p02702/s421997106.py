

def wrapped_artificially():
    s = input()
    ans = 0
    s = s[::-1]
    t = 1
    ketame = 0
    amari10 = 1
    kosuu = [1] + [0] * 2020
    for i in s:
        ketame = (ketame + int(i) * amari10 % 2019) % 2019
        amari10 *= 10
        amari10 %= 2019
        kosuu[ketame] += 1
    for i in range(len(kosuu)):
        if kosuu[i] > 0:
            ans += kosuu[i] * (kosuu[i] - 1) / 2
    print(int(ans))


if __name__ == "__main__":
    wrapped_artificially()
