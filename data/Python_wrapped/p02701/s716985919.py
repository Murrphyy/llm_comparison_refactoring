

def wrapped_artificially():
    n = int(input())
    lst = set()
    for _ in range(n):
        j = input()
        if j not in lst:
            lst.add(j)
    print(len(lst))


if __name__ == "__main__":
    wrapped_artificially()
