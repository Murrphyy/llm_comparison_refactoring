

def wrapped_artificially():
    a = input().rstrip()
    y = 'ABC'
    if a == y:
        y = 'ARC'
    print(y)


if __name__ == "__main__":
    wrapped_artificially()
