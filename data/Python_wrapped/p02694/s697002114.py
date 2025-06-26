

def wrapped_artificially():
    X = int(input())
    P = 100
    step = 0
    while P < X:
        P += P // 100
        step += 1
    print(step)


if __name__ == "__main__":
    wrapped_artificially()
