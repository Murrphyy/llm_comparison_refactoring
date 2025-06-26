def main():
    A, B, C, D = map(int, input().split())
    turn = 0
    while A > 0 and C > 0:
        if turn == 0:
            C -= B
        else:
            A -= D
        turn = (turn + 1) % 2
    if C <= 0:
        print('Yes')
    else:
        print('No')

def wrapped_artificially():
    main()


if __name__ == "__main__":
    wrapped_artificially()
