

def wrapped_artificially():
    S = input()
    T = input()
    t = T[:len(S)]
    if S == t:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    wrapped_artificially()
