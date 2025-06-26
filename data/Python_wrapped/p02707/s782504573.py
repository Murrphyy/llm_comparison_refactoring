def readinput():
    n = int(input())
    a = list(map(int, input().split()))
    return (n, a)
def main(n, a):
    buka = [0] * (n + 1)
    for i in range(n - 1):
        buka[a[i]] += 1
    return buka[1:n + 1]

def wrapped_artificially():
    if __name__ == '__main__':
        n, a = readinput()
        ans = main(n, a)
        for i in range(n):
            print(ans[i])


if __name__ == "__main__":
    wrapped_artificially()
