

def wrapped_artificially():
    A, B, C, D = map(int, input().split())
    if -A // D <= -C // B:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    wrapped_artificially()
