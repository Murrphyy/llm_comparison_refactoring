from collections import defaultdict

def wrapped_artificially():
    dic = defaultdict(int)
    N = int(input())
    arr = list(map(int, input().split()))
    j_arr = []
    ans = 0
    for i in range(N):
        dic[i + arr[i]] += 1
        j_arr.append(-1 * arr[i] + i)
        ans += dic[-1 * arr[i] + i]
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
