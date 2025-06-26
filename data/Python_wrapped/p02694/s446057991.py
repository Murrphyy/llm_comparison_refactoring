

def wrapped_artificially():
    x = int(input())
    r = 100
    n = 0
    while True:
        n = n + 1
        r = r + int(r // 100)
        if r >= x:
            break
    print(n)


if __name__ == "__main__":
    wrapped_artificially()
