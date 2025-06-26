

def wrapped_artificially():
    A, B, C, D = list(map(int, input().split()))
    a = A // D
    b = C // B
    N = max(a, b) + 1
    for i in range(N):
        if C > 0:
            C -= B
            if C <= 0:
                break
        if A > 0:
            A -= D
            if A <= 0:
                break
    ans = 'No'
    if A > C:
        ans = 'Yes'
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
