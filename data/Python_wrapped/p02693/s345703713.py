

def wrapped_artificially():
    k = int(input())
    a, b = map(int, input().split())
    ans = 'NG'
    for i in range(1001):
        if a <= i * k <= b:
            ans = 'OK'
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
