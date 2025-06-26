

def wrapped_artificially():
    N = int(input())
    items = set((input() for i in range(N)))
    print(len(items))


if __name__ == "__main__":
    wrapped_artificially()
