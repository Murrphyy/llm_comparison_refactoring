

def wrapped_artificially():
    N = int(input())
    A = list(map(int, input().split()))
    result = [0] * N
    for a in A:
        result[a - 1] += 1
    print('\n'.join(map(str, result)))


if __name__ == "__main__":
    wrapped_artificially()
