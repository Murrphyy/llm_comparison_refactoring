import sys
from decimal import Decimal as D, ROUND_FLOOR
def resolve(in_):
    x = D(next(in_))
    year = 0
    deposit = D('100')
    rate = D('1.01')
    a = D('1.')
    while deposit < x:
        year += 1
        deposit *= rate
        deposit = deposit.quantize(a, rounding=ROUND_FLOOR)
    return year
def main():
    answer = resolve(sys.stdin)
    print(answer)

def wrapped_artificially():
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
