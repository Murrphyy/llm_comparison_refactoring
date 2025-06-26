

def wrapped_artificially():
    a = list(map(int, input().split()))
    if a[3] <= a[0]:
        print(a[3])
    elif a[3] <= a[0] + a[1]:
        print(a[0])
    else:
        print(a[0] - (a[3] - a[0] - a[1]))


if __name__ == "__main__":
    wrapped_artificially()
