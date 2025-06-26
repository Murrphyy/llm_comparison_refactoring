from collections import defaultdict

def wrapped_artificially():
    n = int(input())
    dic = defaultdict(int)
    for _ in range(n):
        tmp = input()
        dic[tmp] += 1
    print(len(dic))


if __name__ == "__main__":
    wrapped_artificially()
