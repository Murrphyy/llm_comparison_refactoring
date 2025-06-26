import re
def main():
    S = input()
    T = input()
    if re.match('^[a-z]*$', S) and re.match('^[a-z]*$', T) and (1 <= len(S)) and (len(S) <= 10) and (len(T) == len(S) + 1) and (T[0:len(T) - 1] == S):
        print('Yes')
    else:
        print('No')

def wrapped_artificially():
    main()


if __name__ == "__main__":
    wrapped_artificially()
