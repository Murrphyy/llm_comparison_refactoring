

def wrapped_artificially():
    N = int(input())
    A = list(map(int, input().split()))
    Buka = [0] * (N + 1)
    for a in A:
        Buka[a] += 1
    for i in range(1, N + 1):
        print(Buka[i])


if __name__ == "__main__":
    wrapped_artificially()
