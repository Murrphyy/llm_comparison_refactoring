

def wrapped_artificially():
    k = int(input())
    A, B = map(int, input().split())
    print('OK' if A <= B - B % k else 'NG')


if __name__ == "__main__":
    wrapped_artificially()
