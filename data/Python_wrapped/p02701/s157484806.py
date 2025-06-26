import collections

def wrapped_artificially():
    n = int(input())
    box = []
    for i in range(n):
        tmp = str(input())
        box.append(tmp)
    l = len(collections.Counter(box))
    print(l)


if __name__ == "__main__":
    wrapped_artificially()
