

def wrapped_artificially():
    print(*{'ABC', 'ARC'} - {input()})


if __name__ == "__main__":
    wrapped_artificially()
