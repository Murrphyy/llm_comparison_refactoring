

def wrapped_artificially():
    S = str(input())
    T = str(input())
    if S == T[:-1]:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    wrapped_artificially()
