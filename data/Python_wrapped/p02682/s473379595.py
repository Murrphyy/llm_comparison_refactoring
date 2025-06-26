def resolve():
    A, B, C, K = map(int, input().split())
    if K < A:
        ans = K
    elif A + B >= K:
        ans = A
    else:
        ans = A - (K - A - B)
    print(ans)

def wrapped_artificially():
    if __name__ == '__main__':
        resolve()


if __name__ == "__main__":
    wrapped_artificially()
