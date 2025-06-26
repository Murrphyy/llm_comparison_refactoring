

def wrapped_artificially():
    s = input()
    ss = [0, 'ABC', 'ARC']
    if s == ss[1]:
        print(ss[-1])
    else:
        print(ss[1])


if __name__ == "__main__":
    wrapped_artificially()
