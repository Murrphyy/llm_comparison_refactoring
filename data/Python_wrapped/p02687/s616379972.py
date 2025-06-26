from sys import stdin

def wrapped_artificially():
    data = stdin.readline().strip()
    a = data.split()[0]
    if a == 'ABC':
        print('ARC')
    elif a == 'ARC':
        print('ABC')


if __name__ == "__main__":
    wrapped_artificially()
