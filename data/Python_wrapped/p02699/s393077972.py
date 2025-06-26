def main():
    S, W = map(int, input().split(' '))
    if S > W:
        print('safe')
    else:
        print('unsafe')

def wrapped_artificially():
    main()


if __name__ == "__main__":
    wrapped_artificially()
