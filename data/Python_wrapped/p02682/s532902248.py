

def wrapped_artificially():
    d = input()
    d = d.split()
    a = int(d[0])
    b = int(d[1])
    c = int(d[2])
    k = int(d[3])
    f = 0
    if a < k:
        f = f + a
        k = k - a
        if b < k:
            k = k - b
            f = f - k
        else:
            f = f
    else:
        f = k
    print(f)


if __name__ == "__main__":
    wrapped_artificially()
