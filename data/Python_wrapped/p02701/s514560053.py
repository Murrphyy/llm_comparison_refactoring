

def wrapped_artificially():
    N = int(input())
    print(len({input() for _ in range(N)}))


if __name__ == "__main__":
    wrapped_artificially()
