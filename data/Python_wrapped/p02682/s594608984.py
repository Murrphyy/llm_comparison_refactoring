

def wrapped_artificially():
    A, B, C, K = map(int, input().split())
    s0m = 0
    x = max(0, A - K)
    if x == 0:
        s0m = +A
        K = K - A
    else:
        s0m = +K
        K = 0
    if K == 0:
        print(s0m)
    else:
        y = max(0, B - K)
        if y == 0:
            K = K - B
        else:
            K = 0
        if K == 0:
            print(s0m)
        else:
            z = max(0, C - K)
            if z == 0:
                s0m = s0m - C
            else:
                s0m -= K
            print(s0m)


if __name__ == "__main__":
    wrapped_artificially()
