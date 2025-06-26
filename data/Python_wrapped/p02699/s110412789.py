

def wrapped_artificially():
    a = input()
    a = a.split()
    x = int(a[0])
    y = int(a[1])
    if x > y:
        print('safe')
    else:
        print('unsafe')


if __name__ == "__main__":
    wrapped_artificially()
