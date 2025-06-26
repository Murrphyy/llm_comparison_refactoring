

def wrapped_artificially():
    print(['safe', 'unsafe'][eval(input().replace(' ', '<='))])


if __name__ == "__main__":
    wrapped_artificially()
