

def wrapped_artificially():
    n = int(input())
    a = list(map(int, input().split()))
    result = [0] * n
    for i in range(len(a)):
        result[a[i] - 1] += 1
    for i in range(len(result)):
        print(result[i])


if __name__ == "__main__":
    wrapped_artificially()
