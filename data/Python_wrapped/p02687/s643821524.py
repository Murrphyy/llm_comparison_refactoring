def main():
    s = input()
    if s[1] == 'B':
        print('ARC')
    else:
        print('ABC')

def wrapped_artificially():
    main()


if __name__ == "__main__":
    wrapped_artificially()
