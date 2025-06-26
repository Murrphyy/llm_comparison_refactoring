from decimal import Decimal

def wrapped_artificially():
    k = int(input())
    num = 100
    ans = 0
    while k > num:
        num = int(Decimal(num) * Decimal(101) / Decimal(100))
        ans += 1
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
