

def wrapped_artificially():
    a = str(input())
    if a == 'ABC':
        print('ARC')
    elif a == 'ARC':
        print('ABC')


if __name__ == "__main__":
    wrapped_artificially()
