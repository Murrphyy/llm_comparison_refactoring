

def wrapped_artificially():
    N = int(input())
    dict = {}
    for i in range(N):
        dict[input()] = 0
    print(len(dict.keys()))


if __name__ == "__main__":
    wrapped_artificially()
