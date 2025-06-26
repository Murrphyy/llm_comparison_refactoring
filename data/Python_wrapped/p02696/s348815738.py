import sys
from math import floor
def main():
    a, b, n = map(int, input().split())
    if n < b:
        x = n
    else:
        x = b - 1
    r = floor(a * x / b) - a * floor(x / b)
    print(r)

def wrapped_artificially():
    read = sys.stdin.read
    readlines = sys.stdin.readlines
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
