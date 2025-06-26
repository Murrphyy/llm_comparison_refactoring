

def wrapped_artificially():
    print(['No', 'Yes'][input() == input()[:-1]])


if __name__ == "__main__":
    wrapped_artificially()
