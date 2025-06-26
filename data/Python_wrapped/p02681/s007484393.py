

def wrapped_artificially():
    s = list(input())
    t = list(input())
    t.pop()
    if s == t:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    wrapped_artificially()
