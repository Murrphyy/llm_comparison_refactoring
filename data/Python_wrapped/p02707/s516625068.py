from collections import Counter

def wrapped_artificially():
    a = int(input())
    num_list = list(map(int, input().split()))
    D = Counter(num_list)
    for i in range(a):
        print(D[i + 1])


if __name__ == "__main__":
    wrapped_artificially()
