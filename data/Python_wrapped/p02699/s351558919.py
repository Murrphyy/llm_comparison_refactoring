import sys

def wrapped_artificially():
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    S, W = map(int, readline().split())
    if S > W:
        print('safe')
    else:
        print('unsafe')


if __name__ == "__main__":
    wrapped_artificially()
