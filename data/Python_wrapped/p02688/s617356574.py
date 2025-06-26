

def wrapped_artificially():
    word = list(map(int, input().split()))
    dlist = [0] * word[1]
    Alist = [0] * word[1]
    for i in range(word[1]):
        dlist[i] = int(input())
        Alist[i] = list(map(int, input().split()))
    ninzu = [0] * word[0]
    for j in range(word[1]):
        for k in range(dlist[j]):
            ninzu[Alist[j][k] - 1] += 1
    print(ninzu.count(0))


if __name__ == "__main__":
    wrapped_artificially()
