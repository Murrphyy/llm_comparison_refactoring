

def wrapped_artificially():
    a, b = map(int, input().split())
    w = []
    t = {}
    for i in range(b):
        c = int(input())
        s = list(map(int, input().split()))
        w += s
    t = set(w)
    print(a - len(t))


if __name__ == "__main__":
    wrapped_artificially()
