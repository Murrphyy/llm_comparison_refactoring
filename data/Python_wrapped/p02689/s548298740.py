def main():
    n, m = map(int, input().split())
    h_lst = list(map(int, input().split()))
    ok_lst = [1 for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        if h_lst[a] <= h_lst[b]:
            ok_lst[a] = 0
        if h_lst[b] <= h_lst[a]:
            ok_lst[b] = 0
    ans = sum(ok_lst)
    print(ans)

def wrapped_artificially():
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
