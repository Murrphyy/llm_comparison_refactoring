

def wrapped_artificially():
    list = ['ABC', 'ARC']
    s = input()
    i = list.index(s)
    answer = list[1 - i]
    print(answer)


if __name__ == "__main__":
    wrapped_artificially()
