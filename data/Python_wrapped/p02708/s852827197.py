def modinv(a, mod=10 ** 9 + 7):
    return pow(a, mod - 2, mod)

def wrapped_artificially():
    '\nCreated on Sun Jul  5 00:28:02 2020\n\n@author: Aruto Hosaka\n'
    mod = 10 ** 9 + 7
    N, K = map(int, input().split())
    ans1 = N + 1
    ans1 *= N + K + 1
    ans1 %= mod
    ans1 *= N + 2 - K
    ans1 %= mod
    ans1 *= modinv(2)
    ans1 %= mod
    ans2 = N + 1
    ans2 *= N + 2
    ans2 %= mod
    ans2 *= 2 * N + 3
    ans2 %= mod
    ans2 *= modinv(6)
    ans2 %= mod
    ans3 = K - 1
    ans3 *= K
    ans3 %= mod
    ans3 *= 2 * K - 1
    ans3 %= mod
    ans3 *= modinv(6)
    ans3 %= mod
    ans4 = N + 2 - K
    ans = ans1 - ans2 + ans3 + ans4
    ans %= mod
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
