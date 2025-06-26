

def wrapped_artificially():
    S = list(input())
    T = list(input())
    del T[-1]
    if S == T:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    wrapped_artificially()
