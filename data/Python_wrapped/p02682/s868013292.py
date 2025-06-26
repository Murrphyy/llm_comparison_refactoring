

def wrapped_artificially():
    A, B, C, K = map(int, input().split())
    ans = 0
    if A >= K:
        ans = K
    elif A < K and A + B >= K:
        ans = A
    else:
        ans = A - (K - A - B) * 1
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
