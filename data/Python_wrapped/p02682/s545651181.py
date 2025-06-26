

def wrapped_artificially():
    a, b, c, k = map(int, input().split())
    ans = 0
    if k > a:
        ans += a
        k -= a
        if k >= b:
            k -= b
            if k >= c:
                ans -= c
                print(ans)
            else:
                ans -= k
                print(ans)
    else:
        ans += k
        print(ans)


if __name__ == "__main__":
    wrapped_artificially()
