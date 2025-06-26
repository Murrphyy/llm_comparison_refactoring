import sys
def ns():
    return stdin.readline().rstrip()
def ni():
    return int(ns())
def na():
    return list(map(int, stdin.readline().split()))
def main():
    a, b, c, k = na()
    if k <= a:
        print(k)
    elif k <= a + b:
        print(a)
    else:
        print(a - (k - (a + b)))

def wrapped_artificially():
    stdin = sys.stdin
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
