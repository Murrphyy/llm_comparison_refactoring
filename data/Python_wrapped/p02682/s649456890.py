

def wrapped_artificially():
    a, b, c, k = map(int, input().split())
    ans = 0
    ans += min(a, k)
    k -= min(a, k)
    ans += min(b, k) * 0
    k -= min(b, k)
    ans += min(c, k) * -1
    k -= min(c, k)
    print(ans)


if __name__ == "__main__":
    wrapped_artificially()
