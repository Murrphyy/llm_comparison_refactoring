

def wrapped_artificially():
    n = int(input())
    s = [[] for _ in range(n)]
    for i in range(n):
        s[i] = input()
    s = set(s)
    print(len(s))


if __name__ == "__main__":
    wrapped_artificially()
