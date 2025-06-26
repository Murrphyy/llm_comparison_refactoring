import sys

def wrapped_artificially():
    X = int(input())
    if not 101 <= X <= 10 ** 18:
        sys.exit()
    base = 100
    count = 0
    while base < X:
        base += base // 100
        count += 1
    print(count)


if __name__ == "__main__":
    wrapped_artificially()
