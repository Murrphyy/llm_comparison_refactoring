

def wrapped_artificially():
    s = input()
    t = input()
    if len(s) + 1 != len(t):
        print('No')
        exit()
    for i in range(len(s)):
        if s[i] != t[i]:
            print('No')
            exit()
    print('Yes')


if __name__ == "__main__":
    wrapped_artificially()
