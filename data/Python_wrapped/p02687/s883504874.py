import sys
def rs():
    return sys.stdin.readline().rstrip()
def ri():
    return int(rs())
def rs_():
    return [_ for _ in rs().split()]
def ri_():
    return [int(_) for _ in rs().split()]

def wrapped_artificially():
    S = rs()
    print('ARC' if S == 'ABC' else 'ABC')


if __name__ == "__main__":
    wrapped_artificially()
