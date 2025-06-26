

def wrapped_artificially():
    s = input()
    t = input()
    flag = 1
    for i in range(len(s)):
        if s[i] != t[i]:
            flag = 0
            break
    if flag == 1:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    wrapped_artificially()
