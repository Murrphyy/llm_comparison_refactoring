def Qb():
    n, k = map(int, input().split())
    ans = set()
    for v in range(k):
        d = int(input())
        ns = [int(v) for v in input().split()]
        for N in ns:
            ans.add(N)
    print(n - len(ans))

def wrapped_artificially():
    if __name__ == '__main__':
        Qb()


if __name__ == "__main__":
    wrapped_artificially()
