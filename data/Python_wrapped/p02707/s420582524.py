def main():
    n = int(input())
    a_lst = list(map(int, input().split()))
    dic = dict()
    for i in range(n - 1):
        if a_lst[i] in dic:
            dic[a_lst[i]] += 1
        else:
            dic[a_lst[i]] = 1
    dic_keys = dic.keys()
    for i in range(1, n + 1):
        if i in dic_keys:
            print(dic[i])
        else:
            print(0)

def wrapped_artificially():
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
