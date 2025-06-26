import collections
def main():
    N = int(input())
    A = list(map(int, input().split()))
    c = collections.Counter(A)
    for i in range(1, N + 1):
        print(c[i])

def wrapped_artificially():
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
