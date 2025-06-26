

def wrapped_artificially():
    a, b = [input() for i in range(2)]
    if a == b[:-1]:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    wrapped_artificially()
