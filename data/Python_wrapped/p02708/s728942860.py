

def wrapped_artificially():
    '\nCreated on Sat Sep 12 19:24:24 2020\n\n@author: liang\n'
    key = 10 ** 9 + 7
    T, K = map(int, input().split())
    N = list(range(T + 1))
    lower = sum(N[:K])
    higher = sum(N[-K::1])
    ans = 0
    ans = (higher - lower + 1) % key
    for i in range(K + 1, T + 2):
        lower += N[i - 1]
        higher += N[-i]
        ans += higher - lower + 1
        ans %= key
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
