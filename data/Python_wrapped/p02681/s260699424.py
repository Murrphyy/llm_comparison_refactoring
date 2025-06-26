def main():
    S = input()
    T = input()
    if S == T[:-1]:
        print('Yes')
    else:
        print('No')

def wrapped_artificially():
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
