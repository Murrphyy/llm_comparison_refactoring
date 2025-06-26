import math
def main():
    str = input()
    if str == 'ABC':
        print('ARC')
    elif str == 'ARC':
        print('ABC')

def wrapped_artificially():
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
