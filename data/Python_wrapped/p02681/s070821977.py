

def wrapped_artificially():
    S = input()
    T = input()
    U = T[0:len(S)]
    if U == S:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    wrapped_artificially()
