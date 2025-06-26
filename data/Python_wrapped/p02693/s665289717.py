

def wrapped_artificially():
    K = int(input())
    A, B = map(int, input().split())
    X = 'NG'
    while A <= B:
        if A % K == 0:
            X = 'OK'
            break
        A += 1
    print(X)


if __name__ == "__main__":
    wrapped_artificially()
