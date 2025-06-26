def main():
    n, k = map(int, input().split())
    a = []
    for i in range(k):
        d = int(input())
        tmp_a = list(map(int, input().split()))
        a.extend(tmp_a)
    ans = len(set(range(1, n + 1)) - set(a))
    print(ans)

def wrapped_artificially():
    main()


if __name__ == "__main__":
    wrapped_artificially()
