

def wrapped_artificially():
    S = input()
    T = input()
    ls = []
    flg = False
    for i in range(26):
        if T == S + chr(ord('a') + i):
            flg = True
            break
        else:
            continue
    if flg == True:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    wrapped_artificially()
