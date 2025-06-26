

def wrapped_artificially():
    S = list(input())
    P = 0
    M = 2019
    D = [0] * M
    D[0] = 1
    X, Y = (0, 1)
    for i in range(len(S)):
        X += Y * int(S[-i - 1])
        X %= M
        P += D[X]
        D[X] += 1
        Y = Y * 10 % M
    print(P)


if __name__ == "__main__":
    wrapped_artificially()
