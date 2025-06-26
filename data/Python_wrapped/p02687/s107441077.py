def resolve():
    S = input()
    if S[1] == 'B':
        print('ARC')
    else:
        print('ABC')

def wrapped_artificially():
    if __name__ == '__main__':
        resolve()


if __name__ == "__main__":
    wrapped_artificially()
