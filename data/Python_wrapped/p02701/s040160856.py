import collections

def wrapped_artificially():
    N = int(input())
    ls = []
    for i in range(N):
        ls.append(input())
    counter = collections.Counter(ls)
    print(len(counter.keys()))


if __name__ == "__main__":
    wrapped_artificially()
