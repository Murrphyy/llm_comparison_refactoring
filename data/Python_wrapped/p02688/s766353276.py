

def wrapped_artificially():
    N, K = map(int, input().split())
    nums = [i for i in range(N)]
    for i in range(K):
        d = int(input())
        s = list(map(int, input().split()))
        for j in s:
            if j - 1 in nums:
                nums.remove(j - 1)
    print(len(nums))


if __name__ == "__main__":
    wrapped_artificially()
