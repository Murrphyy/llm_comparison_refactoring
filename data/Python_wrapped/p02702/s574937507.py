import sys
from collections import Counter

def wrapped_artificially():
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    mod = 2019
    S = readline().decode().rstrip()
    N = len(S)
    S = S[::-1]
    mod_list = [0] * N
    mod_list[0] = int(S[0])
    power = 1
    for i in range(1, N):
        power *= 10
        power %= mod
        mod_list[i] = power * int(S[i]) + mod_list[i - 1]
        mod_list[i] %= mod
    mod_cnt = Counter(mod_list)
    ans = sum((n * (n - 1) // 2 for n in mod_cnt.values())) + mod_cnt[0]
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
