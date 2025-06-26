def solve(s, p=2019):
    s = s[::-1]
    memo = [0] * p
    memo[0] = 1
    ans = 0
    q = 0
    r = 1
    for c in s:
        q = (q + int(c) * r) % p
        ans += memo[q]
        r = 10 * r % p
        memo[q] += 1
    return ans

def wrapped_artificially():
    s = input()
    print(solve(s))


if __name__ == "__main__":
    wrapped_artificially()
