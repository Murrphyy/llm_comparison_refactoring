

def wrapped_artificially():
    n = int(input())
    list = []
    for _ in range(n):
        list.append(input())
    sets = set(list)
    ans = len(sets)
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
