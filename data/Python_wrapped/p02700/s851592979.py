

def wrapped_artificially():
    A, B, C, D = map(int, input().split())
    print('Yes' if (C - 1) // B <= (A - 1) // D else 'No')


if __name__ == "__main__":
    wrapped_artificially()
