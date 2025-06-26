def main():
    N = int(input())
    A = list(map(int, input().split()))
    C = [0] * N
    for a in A:
        C[a - 1] += 1
    for c in C:
        print(c)

def wrapped_artificially():
    main()


if __name__ == "__main__":
    wrapped_artificially()
