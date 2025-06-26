

def wrapped_artificially():
    s = str(input())
    t = str(input())
    if s == t[:len(s)]:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    wrapped_artificially()
