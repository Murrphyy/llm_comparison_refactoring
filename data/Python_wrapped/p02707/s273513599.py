

def wrapped_artificially():
    n = int(input())
    al = list(map(int, input().split()))
    s = [0] * n
    level = 1
    al.sort()
    for i in range(len(al)):
        if al[i] == level:
            s[level - 1] += 1
        elif al[i] >= level:
            level = al[i]
            s[level - 1] += 1
    for j in s:
        print(j)


if __name__ == "__main__":
    wrapped_artificially()
