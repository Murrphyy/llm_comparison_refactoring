import numpy as np

def wrapped_artificially():
    S = input()
    N = len(S)
    mod = [0 for i in range(2019)]
    mod2 = 0
    ten = 1
    for i in range(N - 1, -1, -1):
        s = int(S[i]) * ten
        mod2 += np.mod(s, 2019)
        mod2 = np.mod(mod2, 2019)
        mod[mod2] += 1
        ten = ten * 10 % 2019
    ans = 0
    for i in range(2019):
        k = mod[i]
        if i == 0:
            if k >= 2:
                ans += k * (k - 1) // 2 + k
            else:
                ans += k
        elif k >= 2:
            ans += k * (k - 1) // 2
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
