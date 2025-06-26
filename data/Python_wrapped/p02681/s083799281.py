

def wrapped_artificially():
    S = list(input())
    T = list(input())
    count = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            count += 1
            break
    if count == 0:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    wrapped_artificially()
