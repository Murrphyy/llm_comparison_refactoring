import math

def wrapped_artificially():
    a, b, c, d = map(int, input().split())
    t_turn = math.ceil(c / b)
    a_turn = math.ceil(a / d)
    if t_turn <= a_turn:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    wrapped_artificially()
