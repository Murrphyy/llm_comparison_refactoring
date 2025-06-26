

def wrapped_artificially():
    print(len(set(open(0).read().split())) - 1)


if __name__ == "__main__":
    wrapped_artificially()
