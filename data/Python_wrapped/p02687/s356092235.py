def main():
    S = input()
    if S == 'ABC':
        print('ARC')
    else:
        print('ABC')

def wrapped_artificially():
    main()


if __name__ == "__main__":
    wrapped_artificially()
