import sys
def main():
    a, b, c, k = map(int, input().split())
    r = min(k, a)
    k -= a
    if k > 0:
        k -= b
        if k > 0:
            r -= k
    print(r)

def wrapped_artificially():
    read = sys.stdin.read
    readlines = sys.stdin.readlines
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
