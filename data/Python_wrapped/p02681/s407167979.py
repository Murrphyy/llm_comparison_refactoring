

def wrapped_artificially():
    S = input()
    T = input()
    flag = True
    for i in range(len(S)):
        if S[i] != T[i]:
            flag = False
    if flag:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    wrapped_artificially()
