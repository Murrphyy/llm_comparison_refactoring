def fact(n):
    ans = 1
    for i in range(2, n + 1):
        ans *= i
    return ans
def comb(n, c):
    return fact(n) // (fact(n - c) * c)

def wrapped_artificially():
    a, b, n = map(int, input().split())
    val = min(b - 1, n)
    print(a * val // b - a * (val // b))


if __name__ == "__main__":
    wrapped_artificially()
