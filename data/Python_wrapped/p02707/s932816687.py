

def wrapped_artificially():
    N = int(input())
    A = map(lambda x: x - 1, map(int, input().split()))
    B = [0] * N
    for a in A:
        B[a] += 1
    print('\n'.join(map(str, B)))


if __name__ == "__main__":
    wrapped_artificially()
