

def wrapped_artificially():
    n = int(input())
    alst = list(map(int, input().split()))
    ans = [0 for _ in range(n)]
    for a in alst:
        ans[a - 1] += 1
    print(*ans, sep='\n')


if __name__ == "__main__":
    wrapped_artificially()
