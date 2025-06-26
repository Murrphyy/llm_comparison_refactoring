import bisect

def wrapped_artificially():
    n = int(input())
    a = list(map(int, input().split()))
    a1 = sorted([a[i] - (i + 1) for i in range(n)])
    a2 = sorted([-a[i] - (i + 1) for i in range(n)])
    ans = 0
    for i in range(n):
        left = bisect.bisect_left(a2, a1[i])
        right = bisect.bisect_right(a2, a1[i])
        ans += right - left
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
