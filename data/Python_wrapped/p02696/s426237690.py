

def wrapped_artificially():
    A, B, N = map(int, input().split())
    if N // B == 0:
        ans_i = N
    else:
        ans_i = B * (N // B) - 1
    print(A * ans_i // B - A * (ans_i // B))


if __name__ == "__main__":
    wrapped_artificially()
