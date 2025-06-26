import sys

def wrapped_artificially():
    S, W = map(int, input().split())
    if S > W:
        print('safe')
    else:
        print('unsafe')


if __name__ == "__main__":
    wrapped_artificially()
