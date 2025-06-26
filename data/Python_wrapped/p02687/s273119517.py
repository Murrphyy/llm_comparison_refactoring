import sys
def main():
    s = str(input())
    if s == 'ABC\n':
        print('ARC')
    else:
        print('ABC')

def wrapped_artificially():
    input = sys.stdin.readline
    main()


if __name__ == "__main__":
    wrapped_artificially()
