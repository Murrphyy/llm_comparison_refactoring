from collections import Counter

def wrapped_artificially():
    n = int(input())
    s = [str(input()) for i in range(n)]
    s = Counter(s).most_common()
    print(len(s))


if __name__ == "__main__":
    wrapped_artificially()
