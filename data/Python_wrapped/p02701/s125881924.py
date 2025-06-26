

def wrapped_artificially():
    N = int(input())
    slist = []
    for i in range(N):
        slist.append(input())
    print(len(set(slist)))


if __name__ == "__main__":
    wrapped_artificially()
