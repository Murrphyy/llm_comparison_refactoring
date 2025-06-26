

def wrapped_artificially():
    A, B, N = list(map(int, input().split()))
    if N < B:
        x = N
    else:
        x = B - 1
    ans_1 = A * x // B
    ans_2 = A * (x // B)
    ans = ans_1 - ans_2
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
