

def wrapped_artificially():
    A = input()
    B = input()
    print('Yes' if A == B[:-1] else 'No')


if __name__ == "__main__":
    wrapped_artificially()
