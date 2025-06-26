

def wrapped_artificially():
    A, B, C, K = map(int, input().split())
    ans = min(A, K) - max(0, K - (A + B))
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
