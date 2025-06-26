import itertools

def wrapped_artificially():
    S = input()[::-1]
    m = [0] * len(S)
    tmp = 1
    for i in range(len(S)):
        m[i] = int(S[i]) * tmp % 2019
        tmp = tmp * 10 % 2019
    cum = [0] + [0] * len(S)
    for i in range(1, len(S) + 1):
        cum[i] = (cum[i - 1] + m[i - 1]) % 2019
    d = {}
    ans = 0
    for i in range(len(cum)):
        if cum[i] not in d:
            d[cum[i]] = 1
        else:
            ans += d[cum[i]]
            d[cum[i]] += 1
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
