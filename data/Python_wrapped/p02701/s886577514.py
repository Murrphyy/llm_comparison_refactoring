

def wrapped_artificially():
    n = int(input())
    ans = []
    cnt = 1
    for i in range(n):
        s = input()
        ans.append(s)
    ans.sort()
    for i in range(n - 1):
        if ans[i] != ans[i + 1]:
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    wrapped_artificially()
