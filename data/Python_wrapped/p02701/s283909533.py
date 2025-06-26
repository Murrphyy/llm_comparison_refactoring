

def wrapped_artificially():
    n = int(input())
    num = [input() for _ in range(n)]
    print(len(set(num)))


if __name__ == "__main__":
    wrapped_artificially()
