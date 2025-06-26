

def wrapped_artificially():
    S_ID = input().rstrip()
    T_ID = input().rstrip()
    if T_ID[0:-1] in S_ID and len(S_ID) != len(T_ID):
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    wrapped_artificially()
