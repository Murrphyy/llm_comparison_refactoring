

def wrapped_artificially():
    S = input()
    T = input()
    S = list(S)
    T = list(T)
    b = 0
    for i in range(0, len(S)):
        if not S[i] == T[i]:
            b += 1
    if len(T) == len(S) + 1 and b == 0:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    wrapped_artificially()
